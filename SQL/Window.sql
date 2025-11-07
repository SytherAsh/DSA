-- Show DATABASES
-- USE testdb

Create Table Comapany(
    product_category VARCHAR(100) NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    prodcut_brand VARCHAR(100) NOT NULL,
    product_price int 
);

ALTER TABLE Comapany
Rename TO Company;

Insert into Company VALUES
('Electronics', 'Mobile', 'Samsung', 20000),
('Electronics', 'Laptop', 'Dell', 50000),
('Electronics', 'Tablet', 'Apple', 30000),
('Furniture', 'Sofa', 'IKEA', 15000),
('Furniture', 'Table', 'IKEA', 8000),
('Furniture', 'Chair', 'IKEA', 5000),
('Clothing', 'T-Shirt', 'Nike', 1500),
('Clothing', 'Jeans', 'Levi', 2500),
('Clothing', 'Jacket', 'Adidas', 3500);


--!-- Window Functions with Rank

select * ,
-- last_value(product_price)
-- first_value(product_price)
-- max(product_price)
-- min(product_price)
-- count(product_price)
Sum(product_price)over(
    partition by product_category
    order by product_price desc
    rows between unbounded preceding and CURRENT ROW
    -- range between unbounded preceding and UNBOUNDED FOLLOWING

) as Total_product_price
FROM Company
order BY product_price desc;


--&-- Window Functions with Ntile

select * ,
case when x.product_price >= 50000 then 'High'
     when x.product_price >= 20000 and x.product_price < 50000 then 'Medium'
     else 'Low' end as price_category 
from 
(
Select * ,
ntile(3) over(order by product_price desc) as price_range
from Company ) as x;