from enum import  Enum
class meal_types(Enum):
    BB,HB,FB=range(3)
    def fromString(self,type):
        type = type.upper()
        type = type.replace(' ', '_')
        for key in meal_types._member_map_.keys():
            if key ==type:
                return meal_types._member_map_.get(key)
        return self.BB
