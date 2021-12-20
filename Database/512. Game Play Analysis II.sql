select Activity.player_id,
Activity.device_id

from 
Activity

inner join (select player_id, min(event_date) as date

from Activity

group by player_id)A

on A.player_id = Activity.player_id
and A.date = Activity.event_date
