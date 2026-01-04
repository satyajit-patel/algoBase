# self join
select e.name Employee
from Employee e
join Employee m

on e.managerId = m.id
-- i.e "Find the row where the employee's managerId matches the manager's id."

where e.salary > m.salary

-- https://leetcode.com/problems/employees-earning-more-than-their-managers/?envType=problem-list-v2&envId=db-db1-sql-i