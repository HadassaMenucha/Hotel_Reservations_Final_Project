import database_actions
from ..entities import Reservation

def get_top_agents_reservations_in_country(country):
    query='''select top 10 reservations.*  , guest.* 
        from (
        select r.agent, count(r.agent) as num_reservations
        from dbo.Reservation as r
        join dbo.Guest as g on g.GuestId=r.GuestId
        where g.country = 'PRT'
        group by r.agent) as data
    join Reservation as reservations on data.agent = reservations.agent
    join Guest on Guest.GuestId= reservations.GuestId
    where num_reservations = max(num_reservations) and country=''' + "'" + country + "'"
    result = database_actions.query(query)
    reservations=list([Reservation(line) for line in result])
    return reservations

def reservations_year_range_adr(year, min , max):
    query = ''' 
        select *
        from Reservation as r 
        join guest as g on g.GuestId=r.GuestId
        where year(r.arrival_date)= '''+year+" and r.adr between "+min +" and "+max+" and is_canceled =0 "
    result = database_actions.query(query)
    reservations=list([Reservation(line) for line in result])
    return reservations

def year_most_cancellations():
    query = ''' select _year, num_agent,num_company,num_direct
    from(
        select year(arrival_date) as _year,count(1)as numCancellations,
            count(case when agent !='NULL' then 1 end) as num_agent,
            count(case when company !='NULL' then 1 end) as num_company,
            count(case when direct_booking !='NULL' then 1 end) as num_direct
        from Reservation
        where is_canceled='True'
        group by year(arrival_date)
        ) as data
    where numCancellations=max(numCancellations)'''
    result = database_actions.query(query)
    reservations = list([line for line in result])
    return reservations

