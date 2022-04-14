# Write your MySQL query statement below

# get department monthly average
select sub1.Day as 'pay_month',
       sub1.department_id,
       (CASE
            WHEN sub2.pay_amount < sub1.avg_amount THEN 'higher'
            WHEN sub2.pay_amount = sub1.avg_amount THEN 'same'
            ELSE 'lower'
       end) as 'comparison'
       from
      (select 
       avg(amount) as avg_amount, 
       Employee.department_id,
       substring(pay_date,1,7) as Day
       from Salary
       inner join Employee
       on Salary.employee_id = Employee.employee_id
       group by substring(pay_date,1,7),Employee.department_id) sub1
       
       inner join 
# get monthly average
        (select avg(amount) as pay_amount, 
               substring(pay_date,1,7) as Day
               from Salary
               group by substring(pay_date,1,7)) sub2
               
               on sub1.Day = sub2.Day


       
