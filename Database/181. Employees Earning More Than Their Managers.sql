# Write your MySQL query statement below
select A.name as "Employee"
     from Employee A
     inner join Employee B
     on B.id = A.managerId
     where A.salary > B.salary
     
