from unittest.mock import create_autospec
from food_management.interactors.preferences_interactor import *
from food_management.interactors.presenters.presenter_interface import *
from food_management.interactors.storages.storage_interface import *
import pytest


class TestPreferences:
    def test_given_invalid_meal_id(self):
        meal_id = 22
        user_id=1
        date="22-12-2020"
        items=[{
          "item_id": 1,
          "item_type":"dosa",
          "quantity": 1
        }]
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = PreferenceInteractor(storage)
        storage.validate_meal_id.side_effect = InvalidMealId
        presenter.raise_exception_for_invalid_meal_id.side_effect = NotFound

        with pytest.raises(NotFound):
            interactor.preference_wrapper(user_id=user_id,
                                          meal_id=meal_id,
                                          items=items,
                                          date=date,
                                          presenter=presenter)

        storage.validate_meal_id.\
        assert_called_once_with(meal_id=meal_id)
        presenter.raise_exception_for_invalid_meal_id.assert_called_once()
    
    
    def test_given_invalid_item_id(self):
        meal_id = 22
        user_id=1
        date="22-12-2020"
        items=[{
          "item_id": 1,
          "item_type":"dosa",
          "quantity": 1
        }]
        item_id = 1
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = PreferenceInteractor(storage)
        storage.validate_item_id.side_effect = InvalidItemId
        presenter.raise_exception_for_invalid_item_id.side_effect = NotFound

        with pytest.raises(NotFound):
            interactor.preference_wrapper(user_id=user_id,
                                          meal_id=meal_id,
                                          items=items,
                                          date=date,
                                          presenter=presenter)

        storage.validate_item_id.\
        assert_called_once_with(item_id=item_id)
        presenter.raise_exception_for_invalid_item_id.assert_called_once()
        
        
        
        
    def test_check_if_item_belongs_to_meal(self):
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = PreferenceInteractor(storage)
        storage.check_if_item_belongs_to_meal = True
        
        actual_value = interactor.preference_wrapper(user_id=user_id,
                                                     meal_id:int, items, date:str, presenter:PresenterInterface)              
        storage.add_washing_machine_wise_day_wise_slots.assert_called_once_with(day=day,
                                        washing_machine_id=washing_machine_id,
                                        start_time=start_time,
                                        end_time=end_time) 
     
    
class NotFound(Exception):
    pass