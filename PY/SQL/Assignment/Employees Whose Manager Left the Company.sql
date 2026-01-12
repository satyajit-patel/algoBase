-- select
--     employee_id
-- from
--     Employees
-- where
--     salary < 30000
--     and
--     manager_id is not null
--     and 
--     manager_id not in (
--         select
--             employee_id
--         from
--             Employees
--     )
-- order by employee_id;

-- or (left joins are good for missing values)

select
    e1.employee_id
from 
    Employees e1
    left join
    Employees e2
    on
    e1.manager_id = e2.employee_id
    /*
        i.e it will check
        manager_id 11 - is there employee_id 11 (YES)
        manager_id 06 - is there employee_id 06 (NO)
        manager_id 09 - is there employee_id 09 (YES)

| employee_id | name      | manager_id | salary | employee_id | name    | manager_id | salary |
| ----------- | --------- | ---------- | ------ | ----------- | ------- | ---------- | ------ |
| 3           | Mila      | 9          | 60301  | 9           | Mikaela | null       | 50937  |
| 12          | Antonella | null       | 31000  | null        | null    | null       | null   |
| 13          | Emery     | null       | 67084  | null        | null    | null       | null   |
| 1           | Kalel     | 11         | 21241  | 11          | Joziah  | 6          | 28485  |
| 9           | Mikaela   | null       | 50937  | null        | null    | null       | null   |
| 11          | Joziah    | 6          | 28485  | null        | null    | null       | null   |
    */
where
    e1.salary < 30000
    and
    e1.manager_id is not null
    and
    e2.employee_id is null
order by employee_id;