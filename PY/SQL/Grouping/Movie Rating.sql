(select u.name as results

from Movies as m
join MovieRating as mr
join users as u
on m.movie_id = mr.movie_id and mr.user_id = u.user_id

group by mr.user_id

order by count(mr.rating) desc, u.name

limit 1)

union all

(select m.title as results

from Movies as m
join MovieRating as mr
join users as u
on m.movie_id = mr.movie_id and mr.user_id = u.user_id

where mr.created_at like "2020-02%"

group by mr.movie_id

order by avg(mr.rating) desc, m.title

limit 1);