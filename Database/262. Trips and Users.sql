# Write your MySQL query statement below



select sub1.request_at as 'Day',round(sum(CASE  
             WHEN sub1 .status LIKE 'cancelled%'  THEN  times
              ELSE 0 
           END)/ sum(times),2)  as  "Cancellation Rate"

from 
(
select count(sub.id) as times,sub.request_at,sub.status from (
select Trips.id, Trips.status,Trips.request_at from Trips

inner join Users a
on  a.users_id = Trips.client_id 
inner join Users b
on  b.users_id = Trips.driver_id

where a.banned = 'No' and b.banned = 'No' 
    and Trips.request_at>="2013-10-01" and Trips.request_at<="2013-10-03"
    
    ) sub
    group by sub.request_at,sub.status
    order by sub.request_at
) sub1
group by  sub1.request_at






