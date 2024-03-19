{{ config(
    materialized="table",
    file_format="delta"
) }}

WITH payments AS (
    SELECT *
    FROM {{ ref('stage_payments') }}
),
users AS (
    SELECT *
    FROM {{ ref('stage_users') }}
)
SELECT u.name AS full_name,
       u.city AS city,
       u.gender AS gender,
       u.state,
       p.country AS country_issued,
       p.credit_card_type AS credit_card_type,
       p.time AS transaction_time
FROM payments AS p
INNER JOIN users AS u
ON p.user_id = u.user_id