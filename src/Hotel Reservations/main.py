import pandas as pd
import sys
import os
sys.path.append(os.path.abspath("../data_analysis/"))
from data_analysis import cleaning
def main():
    ''' reading the data from file '''
    data_file = pd.read_csv('hotel_bookings.csv')

    data_file=cleaning.replace_nulls(data_file)
    data_file=cleaning.fix_reservation_date(data_file)
    data_file=cleaning.fix_is_canceled(data_file)



