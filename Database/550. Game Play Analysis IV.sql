
select round((

select count(distinct Activity.player_id) as player_id from Activity

right join (

select player_id, min(event_date) as event_date

from Activity

group by player_id ) A

on A.player_id = Activity.player_id

and DATE_ADD(A.event_date, INTERVAL 1 DAY) = Activity.event_date

having player_id is not null) / count(distinct player_id),2) as "fraction"

from Activity 
