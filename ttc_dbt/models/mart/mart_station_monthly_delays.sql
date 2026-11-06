{{ config(materialized='table') }}

select
    cleaned_station,
    date_trunc('month', occurred_at) as month,
    count(*) as incidents,
    sum(min_delay) as total_delay_minutes
from {{ref('stg_ttc_delays')}}
group by 1, 2