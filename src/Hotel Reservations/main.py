import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import calendar

''' reading the data from file '''
data_file = pd.read_csv('hotel_bookings.csv')
''' replacing the nulls with nan '''
data_file.replace(['none','undefined','-'],'NaN')

''' changing reservation_date to datetime '''
data_file['reservation_status_date'] = pd.to_datetime(data_file['reservation_status_date'])

''' changing the column 'is_canceled' to bool '''
data_file['is_canceled']=data_file['is_canceled'].map({1: True, 0: False})

# ::TODO convert arrival date from Series to int
print(datetime.datetime.fromisocalendar(2003, 10, 5))
data_file['arrival_date_month']=pd.to_datetime(data_file['arrival_date_month'], format='%B').dt.month
# print('year',data_file['arrival_date_year'].to_string(),'month', data_file['arrival_date_month'].to_string() ,'day',data_file['arrival_date_day_of_month'].to_string())
# create_date=lambda year,month,day:datetime.datetime(year,month,day)
# full_date=lambda year, month=data_file['arrival_date_month'], day=data_file['arrival_date_day_of_month']:datetime.datetime.fromisocalendar(year, month, day)
# data_file['arrival_date']=full_date(data_file['arrival_date_year'])
# print(data_file['arrival_date'].head(1))

# ::TODO direct_booking lambda
# is_direct_booking=lambda agent,company: pd.isna(agent.bool()) and pd.isna(company.bool())#how to do for every line seperately
# print(is_direct_booking(data_file['agent'], data_file['company']))
# data_file['direct_booking']=is_direct_booking(data_file['agent'], data_file['company'])
# print(data_file['direct_booking'])
# direct=lambda agent,company: agent
# data_file['direct_booking']= data_file['agent'].map(is_direct_booking(data_file['agent'].item(),data_file['company'].item()))

# ::TODO drop nan columns
# data_file=data_file.loc[:,data_file.isna().mean()<.7]
# print(data_file.isna().mean())
# print(data_file)
# filling nan's
# data_file.price = df.price.fillna(0)
''' visualizing '''
# data_file.plot(kind='scatter' , x='adults', y='required_car_parking_spaces')
# plt.show()
# sns.distplot(data_file['arrival_date_year'], hist=False)
# plt.show()