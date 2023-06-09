import pandas as pd
from data_analysis import cleaning
from sql_dir import database_actions , queries

def main():
    ''' reading the data from file '''
    data_file = pd.read_csv('project/Hotel Reservations Midterm Project/Hotel Reservations Midterm Project/src\Hotel Reservations/hotel_bookings.csv')
    data_file=setup(data_file)
    choice = input('MENU: \n \t1.see the top 10 Reservations for an agent that has the most reservations in a country of your choice along with the Guest information'
                   '\n \t 2.see top 10 the Reservations + Guests for a year of your choice that are within a chosen range and were not canceled.'
                   '\n \t 3.see which year had the most cancellations. How were the cancellations booked - through an agent, company, or directly?')
    try:
        if choice == '1':
            country = input('what country? ')
            result = queries.get_top_agents_reservations_in_country(country)
            for obj in result:
                print(obj)

        elif choice == '2':
            year=input('enter year: ')
            min = input('bottom of range: ')
            max = input('top of range: ')
            result = queries.reservations_year_range_adr(year,min,max)
            for obj in result:
                print(obj)
        elif choice == '3':
            result = queries.year_most_cancellations()
            print(result)
        else:
            raise ValueError()
    except : 
        print('you did not enter a correct number, between 1 and 3')

    cleaning.visualize(data_file)


def setup(data_file):
    data_file = cleaning.replace_nulls(data_file)
    data_file = cleaning.fix_reservation_date(data_file)
    data_file = cleaning.fix_is_canceled(data_file)
    data_file = cleaning.fix_arrival_date(data_file)
    data_file=cleaning.add_direct_booking(data_file)

    database_actions.create_tables_from_df(data_file)
    return data_file

if __name__ == '__main__':
    main()


