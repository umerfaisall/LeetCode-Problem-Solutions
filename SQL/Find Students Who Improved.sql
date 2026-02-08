# Write your MySQL query statement below
with sco as (
     select student_id, subject,
     first_value(score) over (partition by student_id,subject order by exam_date asc) as min_score,
     last_value(score) over (partition by student_id,subject order by exam_date asc) max_scores,
    row_number() over (partition by student_id,subject order by exam_date desc) as rn
    from scores 
) 
select student_id, subject, min_score as first_score, max_scores as latest_score
from sco
where rn = 1 and min_score < max_scores
