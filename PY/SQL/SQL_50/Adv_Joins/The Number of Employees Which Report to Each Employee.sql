select e2.employee_id, e2.name, count(*) reports_count, round(avg(e1.age)) average_age

-- select e1.name, e1.age, e2.name, e2.employee_id
-- | name  | age | name  | employee_id |
-- | ----- | --- | ----- | ----------- |
-- | Bob   | 36  | Hercy | 9           |
-- | Alice | 41  | Hercy | 9           |
from employees e1
    join employees e2
    on e1.reports_to = e2.employee_id

group by e2.employee_id
order by e2.employee_id;