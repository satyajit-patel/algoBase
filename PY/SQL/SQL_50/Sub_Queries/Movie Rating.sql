(select
    u.name as results
from
    users as u
    join
        movierating as m
        on
            u.user_id = m.user_id
group by
    m.user_id
order by
    count(m.user_id) desc, u.name
limit 1)

-- union -- returns only distinct records
union all -- allows duplicate

(select
    m.title as results
from
    movies as m
    join 
        movierating as mr
        on
            m.movie_id = mr.movie_id
where
    created_at like "2020-02%"
group by
    mr.movie_id
order by
    avg(mr.rating) desc, m.title
limit 1)