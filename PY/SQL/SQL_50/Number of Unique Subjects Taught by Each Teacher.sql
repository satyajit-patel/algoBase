-- select teacher_id, count(*) cnt
-- from (
--     select teacher_id, subject_id
--     from Teacher
--     group by teacher_id, subject_id
--     /*
--     | teacher_id | subject_id |
--     | ---------- | ---------- |
--     | 1          | 2          |
--     | 1          | 3          |
--     | 2          | 1          |
--     | 2          | 2          |
--     | 2          | 3          |
--     | 2          | 4          |
--     */
-- ) t
-- group by teacher_id;

-- or
select teacher_id, count(distinct subject_id) cnt
from teacher
group by teacher_id;