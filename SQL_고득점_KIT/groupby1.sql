select  hour
    ,   count(hour) as count
from    
(
    select  cast(date_format(datetime, '%k') as signed) as hour
    from    animal_outs
) as temp
where   hour between 9 and 19
group by hour
order by hour;
