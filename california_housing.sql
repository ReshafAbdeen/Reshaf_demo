-- 1. Pehle database activate karo
USE june_sql_db;
SELECT COUNT(*) FROM california_housing; 

SELECT ocean_proximity, total_rooms, housing_median_age, median_house_value 
FROM california_housing 
LIMIT 5;