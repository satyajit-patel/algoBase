select round(sum(tiv_2016), 2) as tiv_2016
from insurance
where (lat, lon) in ( -- case 1
    select lat, lon
    from insurance
    group by lat, lon
        having count(*) = 1
) and tiv_2015 in ( -- case 2
    -- i.e this sub query returns 1 column and in condition expects 1 column
    select tiv_2015
    from insurance
    group by tiv_2015
        having count(*) > 1
)