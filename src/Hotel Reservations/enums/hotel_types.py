from enum import  Enum
class hotel_types(Enum):
    RESORT_HOTEL,CITY_HOTEL=range(2)
    def fromString(self,type):
        type = type.upper()
        type = type.replace(' ', '_')
        for key in hotel_types._member_map_.keys():
            if key ==type:
                return hotel_types._member_map_.get(key)
        return self.NULL
