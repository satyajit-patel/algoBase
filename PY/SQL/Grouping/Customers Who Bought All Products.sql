-- select c.customer_id
-- from Customer as c
-- join Product as p 
-- group by customer_id
-- having count(distinct c.product_key) = count(distinct p.product_key)

select customer_id
from Customer
group by customer_id
having count(distinct product_key) = (select count(*) from Product);


-- https://leetcode.com/problems/customers-who-bought-all-products/description/?envType=problem-list-v2&envId=db-db3-grouping-aggregation