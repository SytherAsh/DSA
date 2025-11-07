-- SHOW DATABASES;
-- USE testdb;
-- SHOW TABLES;
-- DROP TABLE employee;

CREATE TABLE employee(
    id INT PRIMARY KEY,
    name VARCHAR(100),
    manageer_id INT
);

INSERT INTO employee VALUES
(101, 'John Doe', 103),
(102, 'Jane Smith', 104),
(103, 'Mike Johnson', NULL),
(104, 'Emily Davis', 103);

SELECT a.name as manageer_name,b.name as employee_name  
FROM employee as a
JOIN employee as b
ON a.id = b.manageer_id;

--todo VIEWS

CREATE VIEW viewEmployee AS
SELECT id,name FROM employee;

SELECT * FROM viewEmployee;

--todo VIEWS


-- CREATE table city(
--     id INT PRIMARY KEY,
--     name VARCHAR(100),
--     population INT,
--     area FLOAT,
--     CONSTRAINT check_population CHECK(population > 100)
--     )

-- INSERT INTO city(id,name,population,area) VALUES
-- (1, 'New York', 8419600, 468.9),
-- (2, 'Los Angeles', 3980400, 503),
-- (3, 'Chicago', 2716000, 227.3),
-- (4, 'Houston', 2328000, 637.4);

-- INSERT INTO city(id,name,population,area) 
-- VALUES
-- (5, 'Phoenix', 1690000, 517.6),
-- (6, 'Philadelphia', 1584200, 142.7),
-- (7, 'San Antonio', 1547000, 465.4),
-- (8, 'San Diego', 1424000, 372.4),
-- (9, 'Dallas', 1343000, 343.3),
-- (10, 'San Jose', 1035000, 180.5);

-- INSERT INTO city(id,name,population,area)
-- VALUES
-- (11, 'New York', 964000, 326.5),
-- (12, 'Dallas', 911500, 874.6),
-- (13, 'New York', 909000, 342.2),
-- (14, 'Dallas', 898000, 223.1),
-- (15, 'New York', 885000, 305.3);



SELECT name 
FROM city
WhERE area > 500
ORDER BY population DESC;
-- LIMIT 5;


Select name,area
from city
where area BETWEEN 200 and 500;
-- where name in ("New York", "Los Angeles");

SELECT AVG(population) as avg_population
FROM city;


SHOW TABLES;