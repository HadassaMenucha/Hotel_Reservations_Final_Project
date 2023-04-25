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
    # data_file = pd.read_csv('hotel_bookings.csv')
    # # print(data_file)
    # data_file=cleaning.replace_nulls(data_file)
    # data_file=cleaning.fix_reservation_date(data_file)
    # data_file=cleaning.fix_is_canceled(data_file)
    # print('b4 connection')
    # database_actions.create_tables_from_df(data_file)
    # print('after connection')
    print(customer_types.CONTRACT.fromString('transient'))


if __name__ == '__main__':
    main()


