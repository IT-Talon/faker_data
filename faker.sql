CREATE TABLE faker (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT,
    phone_number VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    address TEXT,
    gender VARCHAR(10)
);
