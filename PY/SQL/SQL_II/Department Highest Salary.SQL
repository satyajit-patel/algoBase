-- select t2.name Department, t1.name Employee, t1.salary Salary
-- -- select *

-- from Employee t1
-- join Department t2
-- on t1.departmentId = t2.id

-- where t1.salary = (
--     select max(salary)
    
--     from Employee e

--     where e.departmentId = t2.id 
-- );


SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
WHERE (e.departmentId, e.salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee
    GROUP BY departmentId
);
