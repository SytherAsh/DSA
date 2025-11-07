-- USE testdb
SHOW TABLES

drop table employees

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    department VARCHAR(100)
);

INSERT INTO employees (id, name, age, department) VALUES
(1, 'John Doe', 30, 'HR'),
(2, 'Jane Smith', 25, 'IT'),
(3, 'Mike Johnson', 35, 'Finance'),
(4, 'Emily Davis', 28, 'Marketing'),
(5, 'Chris Brown', 40, 'Sales'),
(6, 'Sarah Wilson', 32, 'IT'),
(7, 'David Lee', 29, 'HR'),
(8, 'Laura Taylor', 31, 'Finance'),
(9, 'James Anderson', 27, 'Marketing');


SELECT AVG(age) as average_age
FROM employees;

SELECT name,age 
FROM employees
WHERE age>(SELECT AVG(age) FROM employees);


SELECT * FROM employees;
