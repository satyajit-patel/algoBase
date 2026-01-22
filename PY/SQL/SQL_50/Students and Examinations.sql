select
    stu.student_id,
    stu.student_name,
    sub.subject_name,
    count(ex.subject_name) attended_exams
from
    Students stu
    cross join
        Subjects sub
        left join
            Examinations ex
                on
                sub.subject_name = ex.subject_name
                and
                stu.student_id = ex.student_id
group by
    stu.student_id, stu.student_name, sub.subject_name
    # whatever we write in group by - comes in select as well
order by 
    stu.student_id, 
    sub.subject_name
