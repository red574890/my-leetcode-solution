/* Write your T-SQL query statement below */
select Customers.Name as Customers
       from Customers
       left join Orders
       on Customers.Id = Orders.CustomerId
       WHERE Orders.CustomerId IS NULL;
