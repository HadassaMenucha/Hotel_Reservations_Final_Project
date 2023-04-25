from enum import  Enum
class customer_types(Enum):
    TRANSIENT,CONTRACT,GROUP,TRANSIENT_PARTY,NULL=range(4)
    def fromString(self,type):
        type = type.upper()
        type = type.replace(' ', '_')
        for key in customer_types._member_map_.keys():
            if key ==type:
                return customer_types._member_map_.get(key)
        return self.NULL
