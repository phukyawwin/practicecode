-- You are working for a company that wants to reward its top 10 customers with a free gift. 
-- You have been asked to generate a simple report that returns the top 10 customers by total amount spent ordered from highest to lowest. 
-- Total number of payments has also been requested.

select c.customer_id as customer_id,c.email as email,count(p.payment_id)  as payments_count,
sum(p.amount)::float as total_amount  from 
customer c inner join payment p using (customer_id) group by c.customer_id  order by total_amount desc limit 10;