create or replace view `hive_metastore`.`default`.`stage_users`
  
  
  
  as
    

select user_id AS user_id,
       name AS name,
       city AS city,
       phone_number AS phone_number,
       gender AS gender,
       nationality AS nationality,
       state AS state
from `hive_metastore`.`default`.`users`
