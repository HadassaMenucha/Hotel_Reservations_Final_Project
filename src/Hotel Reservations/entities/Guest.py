from enums import customer_types
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
        self.customer_type=customer_types.fromString(data['customer_type'])

    def __str__(self):
        print('''guest_id: {guest_id}
                adults: {adults}
                children: {children}
                babies: {babies}
                country: {country}
              is_repeated_guest: {is_repeated_guest}
              previous_cancellations: {previous_cancellations}
              previous_booking_not_canceled: {previous_booking_not_canceled}
              customer_type: {customer_type}
                    '''.format(guest_id=self.guest_id, adults=self.adults,children=self.children,
                               babies=self.babies,country=self.country, is_repeated_guest=self.is_repeated_guest
                               ,previous_cancellations=self.previous_cancellations, previous_booking_not_canceled=self.previous_booking_not_canceled
                               ,customer_type=self.customer_type))
