select temp.Department, temp.Employee, temp.Salary
from (
    select d.name as Department, e.name as Employee, e.salary as Salary,
        dense_rank() over(partition by d.name order by e.salary desc) as rnk
    from employee as e join department as d on e.departmentId = d.id
    /*
    | Department | Employee | Salary | rnk |
    | ---------- | -------- | ------ | --- |
    | IT         | Max      | 90000  | 1   |
    | IT         | Joe      | 85000  | 2   |
    | IT         | Randy    | 85000  | 2   |
    | IT         | Will     | 70000  | 3   |
    | IT         | Janet    | 69000  | 4   |
    | Sales      | Henry    | 80000  | 1   |
    | Sales      | Sam      | 60000  | 2   |
    */
) as temp
where temp.rnk <= 3