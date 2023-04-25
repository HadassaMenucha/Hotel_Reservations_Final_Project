import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

def replace_nulls(data_file):
    ''' replacing the nulls with nan '''
    data_file=data_file.replace(['none','undefined','-'],'NaN')
    return data_file
def fix_reservation_date(data_file):
    ''' changing reservation_date to datetime '''
    data_file['reservation_status_date'] = pd.to_datetime(data_file['reservation_status_date'])
    return data_file
def fix_is_canceled(data_file):
    ''' changing the column 'is_canceled' to bool '''
    data_file['is_canceled']=data_file['is_canceled'].map({1: True, 0: False})
    return data_file
def fix_arrival_date(data_file):
    ''' replacing the columns of year, month, day with a column date '''
    data_file['arrival_date_month'] = pd.to_datetime(data_file['arrival_date_month'], format='%B').dt.month
    data_file['arrival_date']=pd.to_datetime(data_file[['arrival_date_year', 'arrival_date_month', 'arrival_date_day_of_month']].rename(columns={'arrival_date_year': 'year', 'arrival_date_month': 'month', 'arrival_date_day_of_month': 'day'}))
    data_file=data_file.drop('arrival_date_month',axis=1)
    data_file=data_file.drop('arrival_date_year',axis=1)
    data_file=data_file.drop('arrival_date_day_of_month',axis=1)
    return data_file

def add_direct_booking(data_file):
    # ::TODO direct_booking lambda
    # is_direct_booking=lambda agent,company: pd.isna(agent.bool()) and pd.isna(company.bool())#how to do for every line seperately
    # print(is_direct_booking(data_file['agent'], data_file['company']))
    # data_file['direct_booking']=is_direct_booking(data_file['agent'], data_file['company'])
    # print(data_file['direct_booking'])
    # direct=lambda agent,company: agent
    # data_file['direct_booking']= data_file['agent'].map(is_direct_booking(data_file['agent'].item(),data_file['company'].item()))
    return data_file

def drop_nan_columns(data_file):
    pass
    # ::TODO drop nan columns
    # data_file=data_file.loc[:,data_file.isna().mean()<.7]
    # print(data_file.isna().mean())
    # print(data_file)
    # filling nan's
    # data_file.price = df.price.fillna(0)

def visualize(data_file):
    ''' visualizing the data '''
    data_file.plot(kind='scatter' , x='adults', y='required_car_parking_spaces')
    plt.show()
    sns.distplot(data_file['arrival_date_year'], hist=False)
    plt.show()