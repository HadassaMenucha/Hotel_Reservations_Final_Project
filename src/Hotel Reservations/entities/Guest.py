class Guest:
    def __init__(self, data):
        self.guest_id=data['guestId']
        self.adults=data['adults']
        self.children=data['children']
        self.babies=data['babies']
        self.country=data['country']
        self.is_repeated_guest=data['is_repeated_guest']
        self.previous_cancellations=data['previous_cancellations']
        self.previous_booking_not_canceled=data['previous_booking_not_canceled']
        self.costomer_type=data['costomer_type']
        self.previous_cancellations=data['previous_cancellations']
