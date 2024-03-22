-- Users Table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    city VARCHAR(100),
    timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
-- Records Table
CREATE TABLE records (
    id SERIAL PRIMARY KEY,
    fk_user_id INT REFERENCES users(id),
    organization_chosen VARCHAR(255),
    description TEXT
);