select p.id,p.name,count(*) as sale_count, 
rank() over (order by count(*) desc) as sale_rank
from people p  join sales s on p.id=s.people_id group by p.id;
