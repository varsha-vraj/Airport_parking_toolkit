
INSERT INTO parking_events (event_id, vehicle_id, zone_id, entry_time, exit_time, paid_amount)
VALUES ('E999', 'V001', 'Z001', '2024-07-19 11:00:00', '2024-07-19 13:00:00', 100.0);
SELECT * FROM parking_events_log ORDER BY log_time DESC;

-- Delete existing logs and test data
DELETE FROM parking_events_log;
DELETE FROM parking_events WHERE event_id = 'E999';
