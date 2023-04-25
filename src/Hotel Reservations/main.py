import pandas as pd
import sys
import os
sys.path.append(os.path.abspath("../enums/"))
from enums.customer_types import customer_types

sys.path.append(os.path.abspath("../data_analysis/"))
from data_analysis import cleaning

# sys.path.append(os.path.abspath("../sql_dir/"))
from sql_dir import database_actions

def main():
    ''' reading the data from file '''
    data_file = pd.read_csv('hotel_bookings.csv')
    setup(data_file)


def setup(data_file):
    data_file = cleaning.replace_nulls(data_file)
    data_file = cleaning.fix_reservation_date(data_file)
    data_file = cleaning.fix_is_canceled(data_file)
    database_actions.create_tables_from_df(data_file)

if __name__ == '__main__':
    main()


