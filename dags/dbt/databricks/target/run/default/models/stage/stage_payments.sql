create or replace view `hive_metastore`.`default`.`stage_payments`
  
  
  
  as
    

select 
CAST(FLOOR(random() * (10000 - 1 + 1)) + 1 AS INTEGER)
 AS id,
       user_id AS user_id,
       case when gender = 'M' then 'male' else 'female' end as gender,
       country_code AS location,
       country AS country,
       credit_card_type AS credit_card_type,
       datetime AS datetime,
       time AS time
from `hive_metastore`.`default`.`payments`
