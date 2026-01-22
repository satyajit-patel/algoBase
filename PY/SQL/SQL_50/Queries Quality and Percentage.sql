select
    query_name,
    round(
        sum(rating / position) # aggregate func gets applied on all rows at once rather that one by one
        / count(query_name), 
    2) quality,
    round(
        sum(rating < 3)
        / count(query_name) 
        * 100, 
    2) poor_query_percentage
from
    Queries
group by query_name;