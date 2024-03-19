{{ config(
    materialized="table",
    file_format="delta"
) }}

WITH payments AS (
    SELECT *
    FROM {{ ref('stage_payments') }}
),
rides AS (
     SELECT *
     FROM {{ ref('stage_rides') }}
)
SELECT r.type AS company_type,
       r.cab_type AS cab_type,
       r.distance_in_miles AS distance_in_miles,
       r.price_in_dollars AS price_usd,
       r.dynamic_fare AS dynamic_fare,
       p.country AS country_issued,
       p.credit_card_type AS credit_card_type,
       p.time AS transaction_time
FROM rides AS r
INNER JOIN payments AS p
ON r.payment_id = p.id