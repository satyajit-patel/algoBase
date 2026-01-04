-- select customer_number, count(*)
select customer_number
from Orders
group by customer_number
order by count(*) desc
limit 1;

# https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/?envType=problem-list-v2&envId=db-db2-filtering-aggregation