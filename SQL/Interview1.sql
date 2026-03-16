-- Online SQL Editor to Run SQL Online.
-- Use the editor to create new tables, insert data and all other SQL operations.

-- second highest amount

select max(amount) from orders 
where amount < (select max(amount) from Orders );

select distinct amount as second_highest_sal from 
( select amount, DENSE_RANK()  over (order by amount desc ) as rnk from orders ) 
where rnk = 2;

-- third highest salary
select distinct amount from
(select amount, DENSE_RANK() over (order by amount desc) as rnk from orders) t
where rnk = 3;

-- third highest Ampunt by country 
select country, amount from
( 
select c.country, o.amount, dense_rank() over (partition by c.country order by o.amount --desc) as rnk from
customers c INNER JOIN orders o
 on c.customer_id = o.customer_id
 ) tbl
 where rnk = 3
 
 

-- second highest amount by country (first and last name)
select first_name, last_name, country, amount from
( 
select c.country, o.amount, c.first_name, c.last_name, dense_rank() over (partition by ----c.country order by o.amount desc) as rnk from
customers c INNER JOIN orders o
on c.customer_id = o.customer_id
) tbl
where rnk = 2

--Retrieve the top 3 first name and lastname basis of amount by country

 
select first_name, last_name, country, amount from
( 
select c.country, o.amount, c.first_name, c.last_name, dense_rank() over (partition by ----c.country order by o.amount desc) as rnk from
customers c INNER JOIN orders o
on c.customer_id = o.customer_id
) tbl
where rnk <= 3



-- Rank employees within each country based on amount.

select c.country, o.amount, c.first_name, c.last_name, dense_rank() over (partition by c.country order by o.amount desc) as rnk from
customers c INNER JOIN orders o
on c.customer_id = o.customer_id;



