-- Create your SELECT statement here
select RANK () OVER ( 
		ORDER BY sum(points) desc
	) rank,  COALESCE(NULLIF(clan,''), '[no clan specified]') AS clan,sum(points) total_points,count(*) total_people from people group by clan;