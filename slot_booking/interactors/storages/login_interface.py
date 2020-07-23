from abc import ABC
from abc import abstractmethod
from slot_booking.constants.enums import *
from .dtos import *

class StorageInterface(ABC):

    @abstractmethod
    def validate_user_name(self, username:str):
        pass
    
    @abstractmethod
    def validate_password(self, username:str, password:str):
        pass
    
    @abstractmethod
    def get_user_role(self, user_id:int):
        pass
    