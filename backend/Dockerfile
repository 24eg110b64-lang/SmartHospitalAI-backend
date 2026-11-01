# ─── Stage 1: Build ───────────────────────────────────────────────────────────
# Eclipse Temurin is the official successor to AdoptOpenJDK.
# jammy = Ubuntu 22.04 LTS — stable, well-supported base.
FROM eclipse-temurin:17-jdk-jammy AS builder

WORKDIR /app

# Copy Maven wrapper and pom.xml first.
# Docker caches this layer separately so dependency downloads are
# only re-run when pom.xml actually changes — speeds up subsequent builds.
COPY .mvn/    .mvn/
COPY mvnw     mvnw
COPY pom.xml  pom.xml

# Ensure the Maven wrapper script is executable on Linux.
# (Windows git does not always preserve the execute bit.)
RUN chmod +x mvnw

# Download all dependencies offline so the next step can build without
# hitting the network again if only source files changed.
RUN ./mvnw dependency:go-offline -B

# Copy full source tree and build the fat JAR.
# -DskipTests avoids running Spring Boot integration tests during the Docker build
# (tests require a live database that is not available at build time).
COPY src/ src/
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
