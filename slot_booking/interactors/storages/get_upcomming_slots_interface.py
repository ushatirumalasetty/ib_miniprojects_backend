from abc import ABC
from abc import abstractmethod
from .dtos import *

class StorageInterface(ABC):

    @abstractmethod
    def get_upcomming_slots(self, user_id:int)->PreviousOrUpcommingSlotsDtoList:
        pass
