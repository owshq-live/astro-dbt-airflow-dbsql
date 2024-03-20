
  
    
        create or replace table `hive_metastore`.`default`.`trusted_rides_km_real`
      
      
    using delta
      
      
      
      
      
      
      
      as
      

WITH trusted_transactions_per_cab_type AS (
    SELECT *
    FROM `hive_metastore`.`default`.`trusted_transactions_per_cab_type`
)
SELECT r.company_type AS company_type,
       r.cab_type AS cab_type,
       r.distance_in_miles AS distance_in_miles,
       (r.distance_in_miles * 1.60934) AS distance_in_km,
       r.price_usd AS price_usd,
       '' AS price_real_brl
FROM trusted_transactions_per_cab_type AS r
  