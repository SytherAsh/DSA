--todo UPDATE ALTER DELETE


USE  testdb;
SHOW TABLES;



CREATE TABLE teacher(
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES dept(id)
);
CREATE table students(
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    department VARCHAR(100)
)
INSERT INTO students (id, name, age, department) VALUES
(1, 'John Doe', 20, 'Computer Science'),
(2, 'Jane Smith', 22, 'Mathematics'),
(3, 'Mike Johnson', 21, 'Physics'),
(4, 'Emily Davis', 23, 'Chemistry');


SELECT * FROM students;


--! UPDATE
SET SQL_SAFER_MODE = 0;

UPDATE students
SET age = 30
WHERE id = 1;

--! ALTER 

--& ADD COLUMN
ALTER TABLE students
ADD COLUMN MERIT INT;

--& RENAME TABLE
ALTER TABLE students
RENAME TO students_info;

--& DROP COLUMN
ALTER TABLE students_info
DROP COLUMN MERIT;

--& RENAME AND CHANGE COLUMN CONDITON
ALTER TABLE students_info
CHANGE COLUMN age student_age INT;

--& CHANGE COLUMN CONDITON
ALTER TABLE students_info
MODIFY age student_age INT


--! DELETE
DELETE  FROM students_info
WHERE student_age>=20;

--! SELECT
Select DISTINCT name from students where age > 20;

-- SHOW DATABASES;
-- DROP table ;
-- SHOW TABLES;
-- DESCRIBE students;
