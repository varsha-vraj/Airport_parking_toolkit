-- Vehicles Table
CREATE TABLE vehicles (
    vehicle_id VARCHAR(10) PRIMARY KEY,
    plate_number VARCHAR(15) UNIQUE NOT NULL,
    type VARCHAR(20),
    owner_name VARCHAR(50)
);

--  Parking Zones Table
CREATE TABLE parking_zones (
    zone_id VARCHAR(10) PRIMARY KEY,
    zone_name VARCHAR(30) NOT NULL,
    rate_per_hour NUMERIC(6,2) NOT NULL,
    is_valet BOOLEAN DEFAULT FALSE
);

-- Parking Events Table
CREATE TABLE parking_events (
    event_id VARCHAR(15) PRIMARY KEY,
    vehicle_id VARCHAR(10) REFERENCES vehicles(vehicle_id),
    zone_id VARCHAR(10) REFERENCES parking_zones(zone_id),
    entry_time TIMESTAMP NOT NULL,
    exit_time TIMESTAMP NOT NULL,
    paid_amount NUMERIC(8,2) CHECK (paid_amount >= 0)
);


CREATE TABLE parking_events_log (
    log_id SERIAL PRIMARY KEY,
    event_id TEXT,
    zone_id TEXT,
    log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

