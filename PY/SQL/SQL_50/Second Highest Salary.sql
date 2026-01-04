/*
-- this fails when table has only 1 row
select distinct salary as SecondHighestsalary

from Employee

order by salary desc

limit 1, 1; -- skip 1 row and return 1 row
*/

-- works
select max(salary) as SecondHighestsalary

from employee

where salary < (
    select max(salary)

    from Employee
);

/*
-- trick to force to return a "null" if no rows are there
select (
    select distinct salary

    from Employee

    order by salary desc

    limit 1 
    offset 1
) as secondHighestsalary;
*/