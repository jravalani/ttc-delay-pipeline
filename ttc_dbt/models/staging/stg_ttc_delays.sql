SELECT
id,
occurred_at,
day,
station,
UPPER(TRIM(SPLIT_PART(station, ' STATION', 1))) AS cleaned_station,
code,
min_delay,
min_gap,
bound,
CASE WHEN line IN ('YU', 'BD', 'SHP') THEN line ELSE 'OTHER' END AS line_group, 
NULLIF(vehicle_id, 0) AS vehicle_id
FROM {{ source('raw', 'ttc_delay_since_2025') }}