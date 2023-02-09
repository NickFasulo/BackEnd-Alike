-- Create database
CREATE DATABASE alike;
-- Create admin user
CREATE USER alike_admin WITH PASSWORD '12345';
-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE alike TO alike_admin;