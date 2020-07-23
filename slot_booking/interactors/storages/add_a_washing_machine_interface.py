from abc import ABC
from abc import abstractmethod
from .dtos import *
from slot_booking.constants.enums import WashingMachineStatus

class StorageInterface(ABC):

    @abstractmethod
    def add_a_washing_machine(self,
                              washing_machine_id:str):
        pass
    
    