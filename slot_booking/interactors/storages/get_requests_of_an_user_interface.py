from abc import ABC
from abc import abstractmethod
from .dtos import *

class StorageInterface(ABC):

    @abstractmethod
    def get_requests_details_of_an_user(self, user_id:int)->RequestCompleteDetailsDto:
        pass
