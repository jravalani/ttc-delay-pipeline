SELECT
id,
occurred_at,
day,
station,
code,
min_delay,
min_gap,
bound,
line,
vehicle_id
FROM {{ source('raw', 'ttc_delay_since_2025') }}