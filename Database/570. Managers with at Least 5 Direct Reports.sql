# Write your MySQL query statement below
select 
       B.name
     from Employee
     
     inner join Employee as B
     on Employee.managerId = B.id
     group by B.id

     having count(Employee.managerId)>=5
