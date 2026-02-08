with cte as(
    select 
        case 
            when MONTHNAME(sale_date) in ('December', 'January', 'February') THEN 'Winter'
            when MONTHNAME(sale_date) in ('March', 'April', 'May') THEN 'Spring'
            when MONTHNAME(sale_date) in ('June', 'July', 'August') THEN 'Summer'
            when MONTHNAME(sale_date) in ('September', 'October', 'November') THEN 'Fall'
        END AS season,
        product_id, 
        quantity, 
        price
from sales 
),
qty as
    (
    select t1.season, 
           p.category, 
           sum(t1.quantity) as total_quantity,
           sum(t1.quantity * t1.price) as total_revenue
    from cte t1
    join products p
    on t1.product_id = p.product_id
    group by season, category
)
select season, 
       category, 
       total_quantity, 
       total_revenue
from (
    select *, 
    row_number() over (partition by season order by total_quantity desc, total_revenue desc, category) as rn from qty
) t
where rn = 1