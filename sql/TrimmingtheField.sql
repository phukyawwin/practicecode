select id,name,
SUBSTR(characteristics, 0,case when POSITION(',' in characteristics)=0 then length(characteristics)+1 else POSITION(',' in characteristics) end) 
as characteristic
from monsters order by id;