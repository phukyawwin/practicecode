with temp as (SELECT DATE(created_at) as day,description FROM events where name='trained')
select day,description,count (*) count from temp group by day,description order by day;