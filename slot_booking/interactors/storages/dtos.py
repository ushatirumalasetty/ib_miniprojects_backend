from datetime import date,datetime
from dataclasses import dataclass
from typing import List
from slot_booking.constants.enums import *

@dataclass
class UserDto:
   user_id:int
   first_name:str
   last_name:str
   user_name:str
   role: UserRole


@dataclass
class WashingMachineDto:
   washing_machine_id:int
   status:WashingMachineStatus

@dataclass
class UserDetailsDto:
   user_id:int
   first_name:str
   last_name:str
   user_name:str

@dataclass
class RequestDetailsDto:
    user_id:int
    date: date
    washing_machine_id: str
    slot_start_time: str
    slot_end_time: str
    request_status: RequestStatus


@dataclass
class RequestCompleteDetailsDto:
    users: List[UserDetailsDto]
    requests:List[RequestDetailsDto]




@dataclass
class SlotStatusDto:
    start_time: str
    end_time: str
    is_avilable: bool

@dataclass
class SlotCompleteStatusDto:
    date: str
    slots: List[SlotStatusDto]

@dataclass
class DateSlotStatusDto:
    date:date
    slots:List[SlotStatusDto]

@dataclass
class DatewiseSlotStatusListDto:
    datewise_slots_list:List[DateSlotStatusDto]

@dataclass
class PreviousOrUpcommingSlotsDto:
    start_time: str
    end_time: str
    washing_machine_slot_id: str
    date: date

@dataclass
class PreviousOrUpcommingSlotsDtoList:
    previous_slots: List[PreviousOrUpcommingSlotsDto]


@dataclass
class WashingMachineWiseSlotDto:
    start_time: str
    end_time: str

@dataclass
class ListWashingMachineWiseSlotDto:
    washing_machine_wise_slots:List[WashingMachineWiseSlotDto]

