-- ============================================================
-- SmartHospitalAI — Database initialisation script
-- ============================================================
-- Run this ONCE on a fresh MySQL instance BEFORE starting the
-- Spring Boot backend for the first time.
--
-- Hibernate (ddl-auto=update) will create the tables automatically
-- from JPA entities.  This script only:
--   1. Creates the database schema.
--   2. Inserts the demo user accounts needed for the login page.
-- ============================================================

CREATE DATABASE IF NOT EXISTS hospital_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE hospital_db;

-- ============================================================
-- Demo users
-- ⚠ Passwords are stored in PLAIN TEXT by the current backend.
--   Rotate these credentials before using in production.
-- ============================================================

INSERT IGNORE INTO users (username, password, role)
VALUES
    ('admin',   'admin123',  'Admin'),
    ('doctor1', 'doctor123', 'Doctor');
