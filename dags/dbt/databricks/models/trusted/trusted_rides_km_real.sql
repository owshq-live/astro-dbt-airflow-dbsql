{{ config(
    materialized="table",
    file_format="delta"
) }}

WITH trusted_transactions_per_cab_type AS (
    SELECT *, CAST(distance_in_miles AS FLOAT) distance_in_miles_flt
    FROM {{ ref('trusted_transactions_per_cab_type') }}
)
SELECT r.company_type AS company_type,
       r.cab_type AS cab_type,
       r.distance_in_miles AS distance_in_miles,
       {{ convert_miles_to_km('r.distance_in_miles_flt') }} AS distance_in_km,
       r.price_usd AS price_usd,
       '' AS price_real_brl
FROM trusted_transactions_per_cab_type AS r
