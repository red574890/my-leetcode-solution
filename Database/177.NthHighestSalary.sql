CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    
    RETURN (
        /* Write your T-SQL query statement below. */
        select distinct Salary from Employee order by Salary desc OFFSET @N-1 rows 
        FETCH NEXT 1 ROWS ONLY
        
    );
END
