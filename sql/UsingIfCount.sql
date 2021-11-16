#calculate the total sales order by orderstatus
#[Shipped,OnHold,InProcess,Resolved,Cancelled,Disputed,Total]
#using if count
select 
	count(if(status='Shipped',1,null))as  'Shipped',
    count(if(status='On Hold',1,null))as  'On Hold', 
    count(if(status='In Process',1,null))as  'In Process',
    count(if(status='Resolved',1,null))as  'Resolved',
    count(if(status='Cancelled',1,null))as  'Cancelled',
    count(if(status='Disputed',1,null))as  'Disputed',
    count(1)as  'Total'
from orders;
