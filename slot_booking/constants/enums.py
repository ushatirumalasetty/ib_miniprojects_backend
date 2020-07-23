from enum import Enum
from ib_common.constants import BaseEnumClass
class Slots(Enum):
    slot1 = "05:00AM - 06:00AM"
    slot2 = "06:00AM - 07:00AM"
    slot3 = "07:00AM - 08:00AM"
    slot4 = "08:00AM - 09:00AM"
    slot5 = "09:00AM - 10:00AM"
    slot6 = "10:00AM - 11:00AM"
    slot7 = "11:00AM - 12:00AM"
    slot8 = "12:00AM - 01:00PM"
    slot9 = "05:00PM - 06:00PM"
    slot10 = "06:00PM - 07:00PM"
    slot11 = "07:00PM - 08:00PM"
    slot12 = "10:00PM - 11:00PM"


class WashingMachines(Enum):
    washing_machine_1 = "washing_machine_1"
    washing_machine_2 = "washing_machine_2"
    washing_machine_3 = "washing_machine_3"
    washing_machine_4 = "washing_machine_4"
    washing_machine_5 = "washing_machine_5"
    washing_machine_6 = "washing_machine_6"
    washing_machine_7 = "washing_machine_7"
    washing_machine_8 = "washing_machine_8"
    washing_machine_9 = "washing_machine_9"
    washing_machine_10 = "washing_machine_10"

class WashingMachineStatus(Enum):
    active="ACTIVE"
    inactive="INACTIVE"

class Days(Enum):
    SUNDAY="SUNDAY"
    MONDAY="MONDAY"
    TUESDAY="TUESDAY"
    WEDNESDAY="WEDNESDAY"
    THURSDAY="THURSDAY"
    FRIDAY="FRIDAY"
    SATuERDAY="SATuERDAY"
    
    
class RequestStatus(Enum):
    APPROVED="APPROVED"
    REJECTED="REJECTED"
    PENDING="PENDING"
    
class UserRole(BaseEnumClass, Enum):
    ADMIN="ADMIN"
    USER="USER"