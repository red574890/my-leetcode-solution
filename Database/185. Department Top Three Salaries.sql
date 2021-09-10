/* Write your T-SQL query statement below */


select A.DepartmentName as Department,
       A.Employee,
       A.Salary
       from(
select Employee.Name as Employee,
       Employee.Salary as Salary,
       Department.Name as DepartmentName,
       Employee.DepartmentId,
       DENSE_RANK() over (  PARTITION BY DepartmentId order by  Salary desc ) AS Rank
       from Employee
       inner join Department 
       on  Employee.DepartmentId = Department.Id   
    )  A
    
    where A.Rank <= 3
  

