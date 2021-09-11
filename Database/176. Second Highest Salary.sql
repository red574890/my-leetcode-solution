/* Write your T-SQL query statement below */

select MAX(e.Salary) as SecondHighestSalary from
 (
select Salary, 
       RANK() over (  order by  Salary desc ) AS Rank  
       from Employee
    ) e
    where e.Rank=2
