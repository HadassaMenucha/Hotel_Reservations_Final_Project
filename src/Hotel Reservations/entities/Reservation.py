from enums.deposit_type import deposit_type 
from enums.hotel_types import hotel_types
from enums.meal_types import meal_types
from . import Guest
class Reservation:
    def enum_format(self,hotel):
        hotel = hotel.upper()
        hotel = hotel.replace('-', '_')
        hotel = hotel.replace(' ', '_')
        return hotel
      
    def __init__(self,data):
        self.reservation_Id=data['ReservationId']
        self.hotel=hotel_types[self.enum_format(data['hotel'])]
        self.is_canceled=data['is_canceled']
        self.lead_time=data['lead_time']
        self.arrival_date=data['arrival_date']
        self.stays_in_weekend_nights=data['stays_in_weekend_nights']
        self.stays_in_week_nights=data['stays_in_week_nights']
        self.meal=meal_types[self.enum_format(data['meal'])]
        self.market_segment=data['market_segment']
        self.distribution_channel=data['distribution_channel']
        self.assigned_room_type = data['assigned_room_type']
        self.reserved_room_type=data['reserved_room_type']
        self.booking_changes=data['booking_changes']
        self.deposit_type=deposit_type[self.enum_format(data['deposit_type'])]
        self.agent=data['agent']
        self.company=data['company']
        self.days_in_waiting_list=data['days_in_waiting_list']
        self.required_car_parking_spaces=data['required_car_parking_spaces']
        self.total_of_special_requests=data['total_of_special_requests']
        self.reservation_status=data['reservation_status']
        self.reservation_status_date=data['reservation_status_date']
        self.guest=Guest.Guest(data,self.enum_format)

    
    
    def __str__(self):
        return (f'''Reservation id: {self.reservation_Id}
                  hotel: {self.hotel}  
                  is_canceled: {self.is_canceled}
                  lead_time: {self.lead_time}
                  arrival_date:{self.arrival_date}
                  stays_in_weekend_nights: {self.stays_in_weekend_nights}
                  meal:{self.meal}
                  market_segment: {self.market_segment}
                  distribution_channel: {self.distribution_channel}
                  assigned_room_type: {self.assigned_room_type}
                  reserved_room_type:{self.reserved_room_type}
                  booking_changes: {self.booking_changes}
                  deposit_type:{self.deposit_type}
                  agent:{self.agent}
                  company: {self.company}
                  days_in_waiting_list: {self.days_in_waiting_list}
                  required_car_parking_spaces: {self.required_car_parking_spaces}
                  total_of_special_requests: {self.total_of_special_requests}
                  reservation_status: {self.reservation_status}
                  reservation_status_date: {self.reservation_status_date}
                  guest: {self.guest}''')


