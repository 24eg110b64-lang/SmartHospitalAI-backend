# ─── Stage 1: Build ───────────────────────────────────────────────────────────
# Eclipse Temurin is the official successor to AdoptOpenJDK.
# jammy = Ubuntu 22.04 LTS — stable, well-supported base.
FROM eclipse-temurin:17-jdk-jammy AS builder

WORKDIR /app

# Copy Maven wrapper and pom.xml first for Docker layer caching.
# Dependencies are only re-downloaded when pom.xml changes.
COPY .mvn .mvn
COPY mvnw pom.xml ./

# Ensure the Maven wrapper script is executable on Linux.
RUN chmod +x mvnw

# Download dependencies offline for fast, reproducible builds.
RUN ./mvnw dependency:go-offline -B

# Copy full application source code.
COPY src ./src

# Build the fat JAR (-DskipTests avoids requiring a live database at build time).
RUN ./mvnw -B package -DskipTests

# ─── Stage 2: Runtime ─────────────────────────────────────────────────────────
# JRE-only image is ~200 MB smaller than the JDK image used for building.
FROM eclipse-temurin:17-jre-jammy

WORKDIR /app

# Copy only the assembled fat JAR from the builder stage.
# artifactId=demo, version=0.0.1-SNAPSHOT → target/demo-0.0.1-SNAPSHOT.jar
COPY --from=builder /app/target/demo-0.0.1-SNAPSHOT.jar app.jar

# Document the default port. Render injects $PORT at runtime and
# application.properties reads it via: server.port=${PORT:8081}
EXPOSE 8081

# -Xmx350m caps the JVM heap below Render's free-tier 512 MB RAM limit.
# Spring Boot reads PORT from the environment automatically.
ENTRYPOINT ["java", "-Xmx350m", "-jar", "app.jar"]
