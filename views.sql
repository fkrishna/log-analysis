create or replace view total_request as
    select count(*) as total, log.time::timestamp::date
    from log 
    group by log.time::timestamp::date;

create or replace view total_request_error as
    select count(*) as total, log.time::timestamp::date
    from log 
    where status != '200 OK'
    group by log.time::timestamp::date
    order by log.time::timestamp::date;

  