select
    if(
        -- if #student is odd(i.e id == lastValue and it's odd) then last person doen't change
        id = (select max(id) from seat) and id&1, id,
        -- else swap the values
        if(id&1, id+1, id-1)
    ) as id, student
from
    seat
order by
    id;