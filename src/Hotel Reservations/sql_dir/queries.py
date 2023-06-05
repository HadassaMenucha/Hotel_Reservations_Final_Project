from . import database_actions
import sys
sys.path.append('..entities/')
# from entities import Reservation
from entities import Reservation
import logging

queryLogger = logging.getLogger('query')
queryLogger.setLevel(logging.INFO)
my_handler=logging.FileHandler('query.log')
queryLogger.addHandler(my_handler)

def get_top_agents_reservations_in_country(country):
    query = ''' 
        select top 10 r.*, g.*
        from Reservation as r
        join guest as g
        on r.GuestId = g.GuestId
        where agent = (
            select top 1 agent
            from Reservation as r
            join Guest as g 
            on r.GuestId = g.GuestId
            where country = ' '''+country +''' '
            group by agent
            order by count(*) desc
            ) '''
    queryLogger.info('get_top_agents_reservations_in_country: query: ' + query)
    result = database_actions.query(query)
    reservations = list([Reservation(line) for line in result])
    queryLogger.info('get_top_agents_reservations_in_country: result: ' + reservations)
    return reservations


def reservations_year_range_adr(year, min, max):
    query = ''' 
        select *
        from Reservation as r 
        join guest as g on g.GuestId=r.GuestId
        where year(r.arrival_date)= ''' + year + " and r.adr between " + min + " and " + max + " and is_canceled =0 "
    queryLogger.info('reservations_year_range_adr: query: ' + query)
    result = database_actions.query(query)
    reservations = result
    # reservations = list([Reservation(line) for line in result])
    queryLogger.info('reservations_year_range_adr: result: ' + reservations)
    return reservations


def year_most_cancellations():
    query = ''' 
                select year(arrival_date) as year, count( case when agent is not null then 1 end ) as agent,
            count( case when company is not null then 1 end ) as company,
            count( case when direct_booking ='Yes' then 1 end ) as direct_booking
            from Reservation
            where year(arrival_date) = (
                select top 1 year(arrival_date) as _year
                from Reservation
                where is_canceled ='True'
                group by year(arrival_date)
                order by  count(*)  desc
            )
            group by year(arrival_date)'''
    queryLogger.info('year_most_cancellations: query: ' + query)
    result = database_actions.query(query)
    # cancellations = list([line for line in result])
    # print(cancellations)
    queryLogger.info('year_most_cancellations: result: ' +str(result))
    return result
