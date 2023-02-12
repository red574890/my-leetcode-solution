# Write your MySQL query statement below

select round(sum(tiv_2016),2) as "tiv_2016" from (
select tiv_2015, 
       tiv_2016,
       lat,
       lon,
       count(*) as times from Insurance
group by lat,lon

having times = 1 

)A

inner join (

select tiv_2015,
        count(tiv_2015) as times
        from Insurance
        group by tiv_2015
        having times>1
) B

on A.tiv_2015 = B.tiv_2015
