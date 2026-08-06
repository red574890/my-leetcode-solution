/* Write your T-SQL query statement below */

with cte as (
select project_id, max(experience_years) as max_experience from 

Project 


inner join  Employee

on Project.employee_id = Employee.employee_id


group by project_id
),


 cte1 as (
select Project.project_id,  Employee.* from 

Project 


inner join  Employee

on Project.employee_id = Employee.employee_id


)


select cte1.project_id,
        cte1.employee_id
 from cte1

inner join cte

on cte.project_id = cte1.project_id

and cte.max_experience = cte1.experience_years
