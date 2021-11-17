-- to create a SELECT statement, this select statement must have NULL handling, using COALESCE and NULLIF

select id,coalesce(nullif(name,''),'[product name not found]') as name,price,
coalesce(nullif(card_name,''),'[card name not found]')as card_name,
card_number,transaction_date from eusales 
where price is not null and price >50;