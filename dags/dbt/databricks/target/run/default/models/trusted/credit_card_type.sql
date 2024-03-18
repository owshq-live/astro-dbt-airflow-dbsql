
  
    
        create or replace table `hive_metastore`.`default`.`credit_card_type`
      
      
    using delta
      
      
      
      
      
      
      
      as
      

WITH payments AS (
    SELECT *
    FROM `hive_metastore`.`default`.`stage_payments`
)
SELECT country AS issued_at,
       credit_card_type AS credit_card_type,
       COUNT(*) AS total_count
FROM payments AS p
GROUP BY country, credit_card_type
  