-- Tenant Table
DROP TABLE IF EXISTS tenant CASCADE;
CREATE TABLE tenant (
    tenant_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    subdomain VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by INT
);

-- Country Table
DROP TABLE IF EXISTS Country CASCADE;
CREATE TABLE Country (
    country_id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by INT,
    country_code VARCHAR(10) UNIQUE NOT NULL,
    country_name VARCHAR(100) NOT NULL
);

-- Location Table
DROP TABLE IF EXISTS Location CASCADE;
CREATE TABLE Location (
    location_id SERIAL PRIMARY KEY,
    country_id INT REFERENCES Country(country_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by INT,
    location_name VARCHAR(255),
    street_name VARCHAR(255)
);

-- User Table
DROP TABLE IF EXISTS Users CASCADE;
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    tenant_id INT REFERENCES tenant(tenant_id) ON DELETE CASCADE,
    country_id INT REFERENCES Country(country_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by INT,
    phone_number VARCHAR(15),
    user_type VARCHAR(50),
    full_name VARCHAR(255)
);

-- Dealer Table
DROP TABLE IF EXISTS Dealer CASCADE;
CREATE TABLE Dealer (
    dealer_id SERIAL PRIMARY KEY,
    tenant_id INT REFERENCES tenant(tenant_id) ON DELETE CASCADE,
    user_id INT REFERENCES Users(user_id),
    country_id INT REFERENCES Country(country_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by INT,
    dealer_name VARCHAR(255),
    phone_number VARCHAR(15)
);

-- Store Table
DROP TABLE IF EXISTS Store CASCADE;
CREATE TABLE Store (
    store_id SERIAL PRIMARY KEY,
    tenant_id INT REFERENCES tenant(tenant_id) ON DELETE CASCADE,
    location_id INT REFERENCES Location(location_id),
    dealer_id INT REFERENCES Dealer(dealer_id),
    country_id INT REFERENCES Country(country_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by INT,
    store_business_name VARCHAR(255),
    store_phone_number VARCHAR(15),
    eff_start_date DATE,
    eff_end_date DATE
);

-- DealerEmployee Table
DROP TABLE IF EXISTS DealerEmployee CASCADE;
CREATE TABLE DealerEmployee (
    dealer_employee_id SERIAL PRIMARY KEY,
    tenant_id INT REFERENCES tenant(tenant_id) ON DELETE CASCADE,
    store_id INT REFERENCES Store(store_id),
    user_id INT REFERENCES Users(user_id),
    country_id INT REFERENCES Country(country_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by INT,
    full_name VARCHAR(255),
    phone_number VARCHAR(15),
    eff_start_date DATE,
    eff_end_date DATE
);

-- Customer Table
DROP TABLE IF EXISTS Customer CASCADE;
CREATE TABLE Customer (
    customer_id SERIAL PRIMARY KEY,
    tenant_id INT REFERENCES tenant(tenant_id) ON DELETE CASCADE,
    user_id INT REFERENCES Users(user_id),
    country_id INT REFERENCES Country(country_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by INT,
    full_name VARCHAR(255)
);

-- StoreToCustomer Table
DROP TABLE IF EXISTS StoreToCustomer CASCADE;
CREATE TABLE StoreToCustomer (
    customer_id INT REFERENCES Customer(customer_id),
    tenant_id INT REFERENCES tenant(tenant_id) ON DELETE CASCADE,
    store_id INT REFERENCES Store(store_id),
    country_id INT REFERENCES Country(country_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by INT,
    eff_start_date DATE,
    eff_end_date DATE,
    PRIMARY KEY (customer_id, store_id)
);

-- Additional tables follow a similar pattern. Let me know if you want the complete set updated!
