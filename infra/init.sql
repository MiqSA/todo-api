CREATE TABLE "user" (
    id SERIAL PRIMARY KEY,
    hashed_id VARCHAR(100) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    hashed_password VARCHAR(100) NOT NULL
);

CREATE TABLE "token" (
    user_id VARCHAR(100) NOT NULL,
    access_token VARCHAR(450) PRIMARY KEY,
    refresh_token VARCHAR(450) NOT NULL,
    status BOOLEAN,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
