import pandas as pd
from data_analysis import cleaning
from sql_dir import database_actions

def main():
    ''' reading the data from file '''
    data_file = pd.read_csv('hotel_bookings.csv')
    setup(data_file)
    cleaning.visualize(data_file)


def setup(data_file):
    data_file = cleaning.replace_nulls(data_file)
    data_file = cleaning.fix_reservation_date(data_file)
    data_file = cleaning.fix_is_canceled(data_file)
    database_actions.create_tables_from_df(data_file)

if __name__ == '__main__':
    main()


