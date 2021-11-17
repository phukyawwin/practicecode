-- to create a SELECT statement that will contain data about departments that had a sale with a price over 98.00 dollars
select  id,name from departments where exists (
	select distinct department_id from sales where
  	departments.id=sales.department_id and price>98.00) order by id;
