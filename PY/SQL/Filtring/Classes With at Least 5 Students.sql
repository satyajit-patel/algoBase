-- Write a solution to find all the classes that have at least five students.
select class
from Courses
group by class
    having count(*) >= 5;

-- Return the result table in any order.

-- https://leetcode.com/problems/classes-with-at-least-5-students/description/?envType=problem-list-v2&envId=db-db2-filtering-aggregation