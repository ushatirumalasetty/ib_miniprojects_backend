from abc import ABC
from abc import abstractmethod
from slot_booking.constants.enums import *
from .dtos import *

class StorageInterface(ABC):

    @abstractmethod
    def get_washing_machine_wise_day_wise_slots(self,
                                                day:Days,
                                                washing_machine_id:str,
                                                limit:int,
                                                offset:int
                                                )->ListWashingMachineWiseSlotDto:
        pass
    
    @abstractmethod
    def validate_washing_machine_id(self, washing_machine_id:int):
        pass
    
    @abstractmethod
    def validate_if_day_belong_to_washing_machine(self, day:Days,
                                     washing_machine_id:int):
        pass
    
    
    