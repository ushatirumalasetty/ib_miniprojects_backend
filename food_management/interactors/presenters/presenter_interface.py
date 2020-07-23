from abc import ABC
from abc import abstractmethod


class PresenterInterface(ABC):
    @abstractmethod
    def raise_exception_for_invalid_meal_id(self):
        pass
    
    @abstractmethod
    def raise_exception_for_invalid_quantity(self, invalid_quantities_list):
        pass
    
    @abstractmethod
    def raise_exception_for_duplicate_item(self, duplicate_item_ids_list):
        pass
    
    @abstractmethod
    def raise_exception_for_invalid_item_for_meal(self):
        pass
    
    @abstractmethod
    def raise_exception_for_invalid_item_id(self):
        pass