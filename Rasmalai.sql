
CREATE DATABASE IF NOT EXISTS  june_sql_db;
-- 2. Computer ko batao ki hum is folder ko use kar rahe hain
USE june_sql_db;
DROP TABLE IF EXISTS test_table;

CREATE TABLE test_table (
    id INT,
    naam VARCHAR(50),
    gmail VARCHAR(100),
    account_id VARCHAR(100),
    gender ENUM ('Male', 'Female', 'other')
    
);

INSERT INTO test_table (id, naam, gmail, account_id, gender)
 VALUES 
 (1, 'Zaynul', 'zaynul@gmail.com', 987654321, 'Male'),
(2, 'Yasin', 'yasin@gmail.com', 987654322, 'Female'),
(3, 'Cutie', 'cutie@gmail.com', 987654323, 'Female');

	SELECT * FROM test_table;