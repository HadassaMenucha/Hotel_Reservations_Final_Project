import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from matplotlib.ticker import MultipleLocator
import matplotlib.ticker as plticker
from pylab import *

debugLogger = logging.getLogger('values')
debugLogger.setLevel(logging.DEBUG)
file_log=logging.FileHandler('cleaning.log')
debugLogger.addHandler(file_log)

def replace_nulls(data_file):
    ''' replacing the nulls with nan '''
    debugLogger.debug('replace_nulls: ')
    debugLogger.debug(data_file)
    data_file=data_file.replace(['none','undefined','-'],'NaN')
    debugLogger.debug('end replace_nulls')
    debugLogger.debug(data_file)
    return data_file
def fix_reservation_date(data_file):
    ''' changing reservation_date to datetime '''
    debugLogger.debug('fix_reservation_date: ')
    debugLogger.debug(data_file)
    data_file['reservation_status_date'] = pd.to_datetime(data_file['reservation_status_date'])
    debugLogger.debug('end fix_reservation_date: ')
    debugLogger.debug(data_file)
    return data_file
def fix_is_canceled(data_file):
    ''' changing the column 'is_canceled' to bool '''
    debugLogger.debug('fix_is_canceled: ')
    debugLogger.debug(data_file)
    data_file['is_canceled']=data_file['is_canceled'].map({1: True, 0: False})
    debugLogger.debug('end fix_is_canceled: ')
    debugLogger.debug(data_file)
    return data_file
def fix_arrival_date(data_file):
    ''' replacing the columns of year, month, day with a column date '''
    debugLogger.debug('fix_arrival_date: ')
    debugLogger.debug(data_file)
    data_file['arrival_date_month'] = pd.to_datetime(data_file['arrival_date_month'], format='%B').dt.month
    data_file['arrival_date']= [datetime.date.replace(datetime.date.today(),year,month,day) for year,month,day in zip(data_file['arrival_date_year'],data_file['arrival_date_month'], data_file['arrival_date_day_of_month'])]
    data_file=data_file.drop('arrival_date_month',axis=1)
    data_file=data_file.drop('arrival_date_year',axis=1)
    data_file=data_file.drop('arrival_date_day_of_month',axis=1)
    debugLogger.debug('end fix_arrival_date: ')
    debugLogger.debug(data_file)
    return data_file

def add_direct_booking(data_file):
    ''' add a column direct_booking based on agent and company values '''
    debugLogger.debug('add_direct_booking: ')
    debugLogger.debug(data_file)
    data_file['direct_booking']= list(map(lambda a , c : 'No' if pd.notna(a) and pd.notna(c) else 'Yes' ,data_file['agent'] , data_file['company']))
    debugLogger.debug('end add_direct_booking: ')
    debugLogger.debug(data_file)
    return data_file

def drop_nan_columns(data_file):
    ''' cleans nans in data file, either drops or fills '''
    debugLogger.debug('drop_nan_columns: ')
    debugLogger.debug(data_file)
    for col in data_file:
        if data_file[col].isna().mean() > .7:
            data_file = data_file.drop(col , axis=1)
        elif 'int' in str(data_file[col].dtype):
            data_file[col].fillna(round(data_file[col].mean()))
        else:
            data_file[col]=data_file[col].map(lambda val:val if not pd.isna(val) else data_file.loc[data_file.index[data_file[col] == val]-1, data_file.index[col]])

    debugLogger.debug('end drop_nan_columns: ')
    debugLogger.debug(data_file)
    return data_file
def visualize(data_file):
    ''' visualizing the data '''

    data_file.plot(kind='scatter' , x='adults', y='required_car_parking_spaces')
    plt.xlabel('adults')
    plt.ylabel('required car parking spaces')
    plt.title('required_car_parking_spaces vs adults')
    plt.show()

    sns.distplot(data_file['children'], hist=False)
    plt.title('number of children')
    plt.xlabel('amount of children')
    plt.ylabel('amount of families')
    plt.show()

    print(data_file.columns)
    plt.boxplot(data_file['stays_in_week_nights'])
    plt.title('stays-in-weekend-nights')
    plt.show()

    data_to_group = data_file[['country','required_car_parking_spaces']]
    grouped_adults = data_to_group.groupby('country').mean()
    grouped_adults=grouped_adults.sort_values(by='required_car_parking_spaces')
    plt.figure(figsize=(28,8))
    sns.barplot(data=grouped_adults, x=grouped_adults.index, y='required_car_parking_spaces', width=5)

    plt.title('average required_car_parking_spaces by country')
    plt.xticks(rotation=90)
    plt.show()