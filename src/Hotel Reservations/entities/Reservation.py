from ..enums import deposit_type , meal_types, hotel_types
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
        # self.adr=data['adr']
        self.required_car_parking_places=data['required_car_parking_places']
        self.total_of_special_requests=data['total_of_special_requests']
        self.reservation_status=data['reservation_status']
        self.reservation_status_date=data['reservation_status_date']
