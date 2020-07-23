from abc import ABC
from abc import abstractmethod

class StorageInterface(ABC):

    @abstractmethod
    def validate_meal_id(self, meal_id:int):
        pass


    @abstractmethod
    def validate_item_id(self, item_id:int):
        pass

    @abstractmethod
    def check_if_item_belongs_to_meal(self, meal_id:int, item_id:int):
        pass
    
    @abstractmethod
    def check_if_preference_exist(self, user_id:int, meal_id:int, date:str):
        pass

    @abstractmethod
    def update_preference(self, user_id:int, meal_id:int,
                                            items,
                                            date:str):
        pass
    
    @abstractmethod
    def create_preference(self, user_id:int,
                                meal_id:int,
                                items,
                                date:str):
        pass
 

    