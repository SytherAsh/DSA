USE testdb;

CREATE TABLE STUDENTS(
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO STUDENTS(id,name) VALUES
(1, 'John Doe'),
(2, 'Jane Smith'),
(3, 'Mike Johnson'),
(4, 'Emily Davis');

CREATE TABLE COURSES(
    id INT PRIMARY KEY,
    course VARCHAR(100)
);

INSERT INTO COURSES(id,course) VALUES
(1, 'Computer Science'),
(2, 'Mathematics'),
(3, 'Physics'),
(4, 'Chemistry');

INSERT INTO COURSES(id,course) VALUES
(5, 'Biology'),
(6, 'History'),
(7, 'Geography'),
(8, 'English');

-- SELECT *
-- FROM STUDENTS as s
-- RIGHT JOIN COURSES as c
-- ON s.id = c.id

-- UNION

SELECT *
FROM STUDENTS as s
LEFT JOIN COURSES as c
ON s.id = c.id