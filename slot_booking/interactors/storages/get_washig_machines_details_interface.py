from abc import ABC
from abc import abstractmethod
from .dtos import *
from typing import List

class StorageInterface(ABC):

    @abstractmethod
    def get_washing_machines_details(self)->List[WashingMachineDto]:
        pass
