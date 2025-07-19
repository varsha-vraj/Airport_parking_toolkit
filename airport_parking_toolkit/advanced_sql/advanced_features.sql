-- ========================================
-- Stored Procedure: Calculate Total Revenue
-- ========================================
CREATE OR REPLACE FUNCTION calculate_total_revenue(start_time TIMESTAMP, end_time TIMESTAMP)
RETURNS NUMERIC AS $$
DECLARE
    total NUMERIC;
BEGIN
    SELECT SUM(paid_amount) INTO total
    FROM parking_events
    WHERE entry_time BETWEEN start_time AND end_time;

    RETURN total;
END;
$$ LANGUAGE plpgsql;

-- Usage:
-- SELECT calculate_total_revenue('2024-07-01', '2024-07-19');



-- ========================
-- Trigger: Log Inserts into parking_events
-- ========================

-- 1. Create log table
CREATE TABLE IF NOT EXISTS parking_log (
    log_id SERIAL PRIMARY KEY,
    event_id TEXT,
    log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    action TEXT
);

-- 2. Trigger function
CREATE OR REPLACE FUNCTION log_parking_event()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO parking_log (event_id, action)
    VALUES (NEW.event_id, 'INSERT');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- 3. Attach trigger to parking_events
DROP TRIGGER IF EXISTS trg_log_insert ON parking_events;

CREATE TRIGGER trg_log_insert
AFTER INSERT ON parking_events
FOR EACH ROW
EXECUTE FUNCTION log_parking_event();



-- ==================================
-- Transaction Example (Atomic Insert)
-- ==================================


BEGIN;

INSERT INTO vehicles (vehicle_id, plate_number, type, owner_name)
VALUES ('V010', 'MH10XY9999', 'SUV', 'Asha Mehta');

INSERT INTO parking_events (event_id, vehicle_id, zone_id, entry_time, exit_time, paid_amount)
VALUES ('E100', 'V010', 'Z001', NOW(), NULL, NULL);



