select *
from Cinema
where (id & 1) and (description != "boring")
order by rating desc;

# https://leetcode.com/problems/not-boring-movies/description/?envType=problem-list-v2&envId=db-db1-sql-i