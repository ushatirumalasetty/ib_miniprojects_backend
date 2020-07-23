from dataclasses import dataclass
from slot_booking.constants.enums import *


@dataclass
class WashingMachineSlotInputDto:
    washing_machine_id : str
    day : Days
    limit : int
    offset : int

