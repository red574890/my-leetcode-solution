# Write your MySQL query statement below
select 
    B.Department,
    Employee.name  as "Employee",
    Employee.salary as "Salary"
    from Employee
    inner join 
   (
    select
    Employee.departmentId as "departmentId",
    Department.name as "Department",
    Employee.name as "Employee",
    max(Employee.salary) as "Salary"
    from Employee
    inner join Department
    on Employee.departmentId = Department.id
    group by Employee.departmentId, Department.name
       )B
    on B.Salary = Employee.salary 
    and B.departmentId = Employee.departmentId
       
