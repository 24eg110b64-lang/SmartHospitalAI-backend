package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.Map;

/**
 * Lightweight health-check endpoint for Render.com (and any load balancer).
 *
 * GET /health → HTTP 200 {"status":"UP"}
 *
 * No Spring Boot Actuator dependency required — this avoids adding ~5 MB of
 * extra JARs and keeps the free-tier memory footprint as small as possible.
 * Render is configured to poll this path via healthCheckPath in render.yaml.
 */
@RestController
public class HealthController {

    @GetMapping("/health")
    public Map<String, String> health() {
        return Map.of("status", "UP");
    }
}
