with cte as 
    (select 
        count(distinct E1.id) as reportees,
        E2.name
from Employee E1 
join Employee E2 
on E1.managerId=E2.id
group by E1.managerId
having reportees>=5 and E1.managerId is not null)
select name from cte;   