{{ config(
    file_format="delta"
) }}

select {{ gen_id() }} AS id,
       user_id AS user_id,
       case when gender = 'M' then 'male' else 'female' end as gender,
       country_code AS location,
       country AS country,
       credit_card_type AS credit_card_type,
       datetime AS datetime,
       time AS time
from {{ source('default', 'payments') }}
