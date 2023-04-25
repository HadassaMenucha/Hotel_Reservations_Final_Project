from ..enums import deposit_type , meal_types, hotel_types
import Guest
class Reservation:
    def __init__(self,data):
        self.reservation_id=data['ReservationId']
        self.hotel=hotel_types.fromString(data['hotel'])
        self.is_canceled=data['is_canceled']
        self.lead_time=data['lead_time']
        self.arrival_date=data['arrival_date']
        self.stay_in_weekend_nights=data['stay_in_weekend_nights']
        self.stays_in_week_nights=data['stays_in_week_nights']
        self.meal=meal_types.fromString(data['meal'])
        self.market_segment=data['market_segment']
        self.distribution_channel=data['distribution_channel']
        self.assigned_room_type = data['assigned_room_type']
        self.reserved_room_type=data['reserved_room_type']
        self.booking_changes=data['booking_changes']
        self.deposit_type=deposit_type.fromString(data['deposit_type'])
        self.agent=data['agent']
        self.company=data['company']
        self.days_in_waiting_list=data['days_in_waiting_list']
        self.required_car_parking_places=data['required_car_parking_places']
        self.total_of_special_requests=data['total_of_special_requests']
        self.reservation_status=data['reservation_status']
        self.reservation_status_date=data['reservation_status_date']
        self.guest=Guest(data)

    def __str__(self):
        print('''Reservation id: {reservation_id}
                  hotel: {hotel}  
                  is_canceled: {is_canceled}
                  lead_time: {lead_time}
                  arrival_date:{arrival_date}
                  stay_in_weekend_nights: {stay_in_weekend_nights}
                  meal:{meal)
                  market_segment: {market_segment}
                  distribution_channel: {distribution_channel}
                  assigned_room_type: {assigned_room_type}
                  reserved_room_type:{reserved_room_type}
                  booking_changes: {booking_changes}
                  deposit_type:{deposit_type}
                  agent:{agent}
                  company: {company}
                  days_in_waiting_list: {days_in_waiting_list}
                  required_car_parking_placesa: {required_car_parking_places}
                  total_of_special_requests: {total_of_special_requests}
                  reservation_status: {reservation_status}
                  reservation_status_date: {reservation_status_date}
                  guest: {guest}
                  
                  '''.format(reservation_id=self.reservation_id ,hotel=self.hotel , is_canceled=self.is_canceled
                         ,lead_time=self.lead_time,arrival_date=self.arrival_date,stay_in_weekend_nights=self.stay_in_weekend_nights
                         ,meal=self.meal,market_segment=self.market_segment,distribution_channel=self.distribution_channel, assigned_room_type=self.assigned_room_type
                             ,reserved_room_type=self.reserved_room_type, booking_changes=self.booking_changes,deposit_type=self.deposit_type,
                             agent=self.agent,company=self.company, days_in_waiting_list=self.days_in_waiting_list, required_car_parking_places=self.required_car_parking_places,
                             total_of_special_requests=self.total_of_special_requests,reservation_status=self.reservation_status,
                             reservation_status_date=self.reservation_status_date, guest=self.guest
                             ))


