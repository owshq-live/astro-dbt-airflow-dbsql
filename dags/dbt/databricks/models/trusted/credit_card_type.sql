{{ config(
    materialized="table",
    file_format="delta"
) }}

WITH payments AS (
    SELECT *
    FROM {{ ref('stage_payments') }}
)
SELECT country AS issued_at,
       credit_card_type AS credit_card_type,
       COUNT(*) AS total_count
FROM payments AS p
GROUP BY country, credit_card_type