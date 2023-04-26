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
    data_file['arrival_date']= [datetime.date.replace(datetime.date.today(),year,month,day) for year,month,day in zip(data_file['arrival_date_year'],data_file['arrival_date_month'], data_file['arrival_date_day_of_month'])]
    data_file=data_file.drop('arrival_date_month',axis=1)
    data_file=data_file.drop('arrival_date_year',axis=1)
    data_file=data_file.drop('arrival_date_day_of_month',axis=1)
    return data_file

def add_direct_booking(data_file):
    ''' add a column direct_booking based on agent and company values '''
    data_file['direct_booking']= list(map(lambda a , c : 'No' if pd.notna(a) and pd.notna(c) else 'Yes' ,data_file['agent'] , data_file['company']))
    return data_file

def drop_nan_columns(data_file):
    # ::TODO nan not numbers fill with top or bottom value
    for col in data_file:
        if data_file[col].isna().mean() > .7:
            data_file = data_file.drop(col , axis=1)
        elif 'int' in str(data_file[col].dtype):
            data_file[col].fillna(round(data_file[col].mean()))
        else:
            data_file[col].fillna(data_file[col])

def visualize(data_file):
    ''' visualizing the data '''
    data_file.plot(kind='scatter' , x='adults', y='required_car_parking_spaces')
    plt.show()
    sns.distplot(data_file['arrival_date_year'], hist=False)
    plt.show()