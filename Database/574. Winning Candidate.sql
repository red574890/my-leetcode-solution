# Write your MySQL query statement below



select sub1.name


from (


select candidateId, count(candidateId) as countid, Candidate.name
from Vote

inner join Candidate 
on Vote.candidateId = Candidate.id
group by candidateId
order by countid desc

) sub1
limit 1
