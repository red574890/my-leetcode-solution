# Write your MySQL query statement below

select  A.question_id as survey_log  
from( 
select action,question_id, count(*) as times
       from SurveyLog
       where action = 'show' or action = 'answer'
       group by action, question_id

        )A
inner join ( 
select action,question_id, count(*) as times
       from SurveyLog
       where action = 'show' or action = 'answer'
       group by action, question_id
        )B
  on A.question_id = B.question_id
  where A.action <> B.action  and A.action = "show"
  order by B.times/A.times desc ,survey_log asc
  limit 1
