from food_management.interactors.storages.storage_interface import StorageInterface
from food_management.interactors.presenters.presenter_interface import PresenterInterface
from dataclasses import dataclass
from typing import List


class PreferenceInteractor:
    def __init__(self, storage:StorageInterface):
        self.storage = storage


    def preference_wrapper(self, user_id:int, meal_id:int, items, date:str, presenter:PresenterInterface):
        try:
            self.preference(user_id=user_id, meal_id=meal_id, items=items, date=date)
        except InvalidMealId:
            presenter.raise_exception_for_invalid_meal_id()
        except InvalidQuantity as err:
            presenter.raise_exception_for_invalid_quantity(err)
        except DuplicateItem as err:
            presenter.raise_exception_for_duplicate_item(err)
        except InvalidItemOfMeal:
            presenter.raise_exception_for_invalid_item_for_meal()
        except InvalidItemId:
            presenter.raise_exception_for_invalid_item_id()


    def preference(self, user_id, meal_id, items, date):
        item_ids_list=[]
        item_quantities_list=[]
        for item in items:
            item_ids_list.append(item.item_id)
            item_quantities_list.append(item.quantity)

        self.storage.validate_meal_id(meal_id)
        self.storage.validate_item_id(item_ids_list)
        self._check_if_duplicate_item_id(item_ids_list)
        self._validate_item_quantity(item_quantities_list)
        self.storage.check_if_item_belongs_to_meal(meal_id, item_ids_list)
        is_already_saved = self.storage.check_if_preference_exist(user_id,
                                                            meal_id, date)
        if is_already_saved:
            self.storage.update_preference(user_id=user_id,
                                           meal_id=meal_id,
                                           items=items,
                                           date=date)
        else:
            self.storage.create_preference(user_id=user_id,
                                           meal_id=meal_id,
                                           items=items,
                                           date=date)


    def _check_if_duplicate_item_id(self, item_ids_list):
        item_ids_list.sort()
        duplicate_item_ids_list=[]

        for i in range (len(item_ids_list)-1):
         	if item_ids_list[i] == item_ids_list[i+1]:
         	    duplicate_item_ids_list.append(item_ids_list[i])

        if duplicate_item_ids_list:
            raise DuplicateItem(duplicate_item_ids_list)


    def _validate_item_quantity(self, item_quantities_list):
        invalid_quantities_list=[]
        for quantity in item_quantities_list:
            if quantity <= 0:
                invalid_quantities_list.append(quantity)
        if invalid_quantities_list:
            raise InvalidQuantity(invalid_quantities_list)




class DuplicateItem(Exception):
    def __init__(self, duplicate_items:List):
        self.duplicate_items = duplicate_items

class InvalidQuantity(Exception):
    def __init__(self, invalid_quantities_list):
        self.invalid_quantities_list=invalid_quantities_list

class InvalidMealId(Exception):
    pass

class InvalidItemOfMeal(Exception):
    pass

class InvalidItemId(Exception):
    pass




@dataclass
class ItemDto:
    item_id : int
    item_type : str
    quantity : int

class ListOfItemDto:
    item_dtos_list : List[ItemDto]
