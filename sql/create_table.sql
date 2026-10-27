CREATE TABLE ttc_delay_since_2025 (
    id INT PRIMARY KEY,
    occurred_at TIMESTAMP,
    day TEXT,
    station TEXT,
    code TEXT,
    min_delay INT,
    min_gap INT,
    bound TEXT,
    line TEXT,
    vehicle_id INT
);