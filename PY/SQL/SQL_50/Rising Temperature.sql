select w1.id

from Weather w1, Weather w2

where 
-- w1.recordDate = date_add(w2.recordDate, interval 1 day)
-- datediff(today's date, previousDay's date)
datediff(w1.recordDate, w2.recordDate) = 1
and w1.temperature > w2.temperature;

-- SELECT w1.id
-- FROM Weather w1
-- JOIN Weather w2
--   ON DATE_SUB(w1.recordDate, INTERVAL 1 DAY) = w2.recordDate
-- WHERE w1.temperature > w2.temperature;