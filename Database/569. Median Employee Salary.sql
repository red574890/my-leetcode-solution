# Write your MySQL query statement below

select Sub2.id,
      Sub2.company,
      Sub2.salary from 

(

select  Employee.id,
        Employee.company,
        Employee.salary,
        row_number() over(partition by Employee.company 
                           order by Employee.salary  ) as rn,
        Sub.number_of_salary  as 'number_of_salary'
        from Employee
        
        
        inner join 
        (select count(salary)/2 as 'number_of_salary',
               company
              from Employee
              group by company) AS Sub
              
              on Sub.company = Employee.company
              
        order by  Employee.company, Employee.salary
) Sub2
where Sub2.rn = if(round(Sub2.number_of_salary)-Sub2.number_of_salary=0,Sub2.number_of_salary,round(Sub2.number_of_salary))
or  Sub2.rn = if(round(Sub2.number_of_salary)-Sub2.number_of_salary=0,Sub2.number_of_salary+1,round(Sub2.number_of_salary))

              
       
       

       
