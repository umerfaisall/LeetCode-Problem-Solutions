SELECT s.user_id, ifnull(round(sum(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END)/count(c.action),2),0) as confirmation_rate
from  signups s
left join confirmations c
on s.user_id = c.user_id
group by s.user_id, c.user_id
order by confirmation_rate