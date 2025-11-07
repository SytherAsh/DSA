CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(10),
    managerId INT
);

INSERT INTO employees (id, name, department, managerId) VALUES
(101, 'John', 'A', NULL),
(102, 'Dan', 'A', 101),
(103, 'James', 'A', 101),
(104, 'Amy', 'A', 101),
(105, 'Anne', 'A', 101),
(106, 'Ron', 'B', 101);

DROP TABLE IF EXISTS employe        es;

select e2.name
from employees as e1 
inner join employees as e2
on e2.id = e1.managerId
group by e1.managerId
having count(e1.managerId)>=5 ;

CREATE table books(
    id INT PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    price DECIMAL(10, 2),
    date_pub DATE
);

INSERT INTO books (id, title, author, price, date_pub) VALUES
(1, 'Book A', 'Author X', 29.99, '2020-01-15'),
(2, 'Book B', 'Author Y', 19.99, '2021-06-20'),
(3, 'Book C', 'Author Z', 39.99, '2019-03-10'),
(4, 'Book D', 'Author X', 24.99, '2022-07-25'),
(5, 'Book E', 'Author Y', 15.99, '2023-08-30');




select *,
extract (year from date_pub) as yearname
from books
order by 
case when yearname= 2023 then 1 
     when yearname= 2022 then 2
     when yearname= 2021 then 3 else 4 
     end ASC;