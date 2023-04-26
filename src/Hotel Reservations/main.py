import pandas as pd
from data_analysis import cleaning
from sql_dir import database_actions

def main():
    ''' reading the data from file '''
    data_file = pd.read_csv('hotel_bookings.csv')
    cleaning.drop_nan_columns(data_file)
    # data_file=setup(data_file)
    # cleaning.visualize(data_file)
    # for x , y  in range (2), range(4):
    #     print(a ,c )
#         ValueError: too many values to unpack (expected 2)
#     for a in range(2) and for c in range(4):
#             print(a,c)
#         NameError: name 'c' is not defined
#     to_iter= dict([[x for x in  range(4)],[y for y in range(4)]])
#     print(to_iter)
#     for a ,b in list(range(4), range(4)):
#         print(a)


def setup(data_file):
    data_file = cleaning.replace_nulls(data_file)
    data_file = cleaning.fix_reservation_date(data_file)
    data_file = cleaning.fix_is_canceled(data_file)
    data_file = cleaning.fix_arrival_date(data_file)
    database_actions.create_tables_from_df(data_file)
    return data_file

if __name__ == '__main__':
    main()


