from enum import  Enum
class deposit_type(Enum):
    NO_DEPOSIT,NON_REFUND,REFUNDABLE=range(3)
    def fromString(self,type):
        type = type.upper()
        type = type.replace(' ', '_')
        for key in deposit_type._member_map_.keys():
            if key ==type:
                return deposit_type._member_map_.get(key)
        return self.NO_DEPOSIT
