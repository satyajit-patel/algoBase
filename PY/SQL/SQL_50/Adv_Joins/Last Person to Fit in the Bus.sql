/*
    employee	category	amount
    Alice	        Tech	500
    Bob	            Tech	300
    Charlie	        Tech	300
    David	        Home	400
    Eve	            Home	200

    SELECT 
        employee, 
        category, 
        amount,
        DENSE_RANK() OVER (PARTITION BY category ORDER BY amount DESC) as dept_rank,
        SUM(amount) OVER (ORDER BY amount DESC) as running_total
    FROM sales;

    employee	category	amount	dept_rank	running_total
    Alice	        Tech	500	    1	        500
    David	        Home	400	    1	        900
    Bob	            Tech	300	    2	        1500
    Charlie	        Tech	300	    2	        1500
    Eve	            Home	200	    2	        1700

    SELECT 
        employee, 
        amount,
        SUM(amount) OVER (ORDER BY amount DESC ROWS UNBOUNDED PRECEDING) as running_total
    FROM sales;

    employee	amount	running_tota
    Alice	    500	    500
    David	    400	    900
    Bob	        300	    1200
    Charlie	    300	    1500
    Eve	200	    1700	1500
*/

-- with temp as (
--     select 
--         person_name,
--         sum(weight) over(order by turn) as running_sum
--     from
--         queue
-- )
-- /*
--     | person_name | running_sum |
--     | ----------- | ----------- |
--     | Alice       | 250         |
--     | Alex        | 600         |
--     | John Cena   | 1000        |
--     | Marie       | 1200        |
--     | Bob         | 1375        |
--     | Winston     | 1875        |
-- */
-- select
--     person_name
-- from
--     temp
-- where
--     running_sum <= 1000
-- order by
--     running_sum desc
-- limit 1

-- or

/*
    we know the turn
    1 >= 1 (running_sum = 250)
    2 >= 1, 2 (running_sum = 600)
    3 >= 1, 2, 3 (running_sum = 1000)
    4 >= 1, 2, 3, 4 (running_sum = 1200) - exceeded the barier
    5 >= 1, 2, 3, 4, 5
    6 >= 1, 2, 3, 4, 5, 6
    so we can use join either
*/
select
    q1.person_name
from
    queue as q1
    join
        queue as q2
        on
            q1.turn >= q2.turn
group by
    q1.turn
    having
        sum(q2.weight) <= 1000
order by
    q1.turn desc
limit 1