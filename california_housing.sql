USE june_sql_db;
-- 1. Jo columns screen par dekhne hain unhe select kiya aur unka math (Aggregation) nikala
SELECT 	
    CASE
        WHEN median_house_value > 300000 THEN 'Luxury Class'
        WHEN median_house_value BETWEEN 150000 AND 300000 THEN 'Middle Class'
        ELSE 'Budget Class'
    END AS house_segment,
    COUNT(*) AS total_house,
    AVG(total_rooms) AS avg_rooms
    
FROM california_housing
GROUP BY 
	CASE 
        WHEN median_house_value > 300000 THEN 'Luxury Class'
        WHEN median_house_value BETWEEN 150000 AND 300000 THEN 'Middle Class'
        ELSE 'Budget Class'
    END;