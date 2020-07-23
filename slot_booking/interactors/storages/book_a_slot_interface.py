from abc import ABC
from abc import abstractmethod
from .dtos import *
from slot_booking.constants.enums import WashingMachineStatus

class StorageInterface(ABC):

    @abstractmethod
    def book_a_slot(self, date, start_time, end_time, user_id:int):
        pass
