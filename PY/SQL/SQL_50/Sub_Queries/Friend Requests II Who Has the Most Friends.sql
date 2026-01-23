-- with temp as (
--     (
--         select
--             requester_id as tot
--         from
--             requestaccepted
--     )
--     union all
--     (
--         select
--             accepter_id as tot
--         from
--             requestaccepted
--     )
-- )
-- select
--     tot as id, count(*) as num
-- from
--     temp
-- group by
--     tot
-- order by
--     num desc
-- limit 1

select t.id, count(*) as num
from (
    select requester_id as id from RequestAccepted
    union all
    select accepter_id as id from RequestAccepted
) as t
group by t.id
order by num desc
limit 1;