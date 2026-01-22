select
    round(
        sum(if(order_date = customer_pref_delivery_date, 1, 0))
        / count(customer_id)
        * 100, 
        2) immediate_percentage
from delivery
where (customer_id, order_date) in (
    select
        customer_id,
        min(order_date) first_order
    from
        delivery
    group by
        customer_id
    /*
    | customer_id | first_order |
    | ----------- | ----------- |
    | 1           | 2019-08-01  |
    | 2           | 2019-08-02  |
    | 3           | 2019-08-21  |
    | 4           | 2019-08-09  |
    */
);