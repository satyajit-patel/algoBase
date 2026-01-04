-- Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.
select 
    -- date_format(trans_date, '%Y-%m') as month, 
    -- left(trans_date, 7) as month,
    substr(trans_date, 1, 7) as month, -- substr(exp, start, length)
    country, 
    count(id) as trans_count, 
    sum(state = "approved") as approved_count,
    sum(amount) as trans_total_amount,  
    sum(if(state = "approved", amount, 0)) as approved_total_amount
from 
    Transactions
group by 
    month, country
-- Return the result table in any order.
-- https://leetcode.com/problems/monthly-transactions-i/description/?envType=problem-list-v2&envId=db-db2-filtering-aggregation