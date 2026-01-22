-- select 
-- e2.name
-- from
--     Employee e1
--     join
--         Employee e2
--         on
--             e1.managerId = e2.id
--             /*
-- We look at every person in E1. If they have a managerId, we go to E2 and find the person whose id matches that number. 
-- Dan (102) says: "My manager is 101."
-- We look at the second table for 101 and find John.
-- Match! We now have a row that says: Dan's manager is John.
-- The computer does this for everyone. Since 5 people (Dan, James, Amy, Anne, Ron) all have managerId = 101, the join creates 5 rows where the manager's name is John.

-- | id  | name  | department | managerId | id  | name | department | managerId |
-- | --- | ----- | ---------- | --------- | --- | ---- | ---------- | --------- |
-- | 106 | Ron   | B          | 101       | 101 | John | A          | null      |
-- | 105 | Anne  | A          | 101       | 101 | John | A          | null      |
-- | 104 | Amy   | A          | 101       | 101 | John | A          | null      |
-- | 103 | James | A          | 101       | 101 | John | A          | null      |
-- | 102 | Dan   | A          | 101       | 101 | John | A          | null      |
--             */
-- group by
--     e1.managerid
--     having
--         count(e1.managerid) >= 5;

select
    name
from
    Employee
where
    id in (
        select
            managerId
        from
            Employee
        group by
            managerId
            having
                count(managerId) >= 5
);