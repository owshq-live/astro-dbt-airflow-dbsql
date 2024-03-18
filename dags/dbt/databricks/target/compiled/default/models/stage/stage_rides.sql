

select id AS id,
       user_id AS user_id,
       payment_id AS payment_id,
       name AS type,
       cab_type AS cab_type,
       source AS source,
       destination AS destination,
       distance AS distance_in_miles,
       price AS price_in_dollars,
       surge_multiplier AS dynamic_fare
       
from `hive_metastore`.`default`.`rides`