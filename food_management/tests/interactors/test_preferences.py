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
        items=[ItemDto(
          item_id= 1,
          item_type="dosa",
          quantity= 1
        )]
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
        items=[ItemDto(
          item_id= 1,
          item_type="dosa",
          quantity= 1
        )]
        item_id = [1]
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
        user_id=1
        meal_id=1
        item_id=[1]
        items=[ItemDto(
          item_id= 1,
          item_type="dosa",
          quantity= 1
        )]
        date="22-12-1996"
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = PreferenceInteractor(storage)
        storage.check_if_item_belongs_to_meal.return_value = True

        interactor.preference_wrapper(user_id=user_id,
                                                     meal_id=meal_id,
                                                     items=items,
                                                     date=date,
                                                     presenter=presenter)
        storage.check_if_item_belongs_to_meal.\
        assert_called_once_with(meal_id=meal_id,item_id=item_id)
    '''    
    def test_create_preference(self):
        user_id=1
        meal_id=1
        items=[ItemDto(
          item_id= 1,
          item_type="dosa",
          quantity= 1
        )]
        date="22-12-1996"
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = PreferenceInteractor(storage=storage)
       
        interactor.preference_wrapper(user_id=user_id,
                                      meal_id=meal_id,
                                      items=items,
                                      date=date,
                                      presenter=presenter)
        storage.create_preference.assert_called_once_with(user_id=user_id,
                                           meal_id=meal_id,
                                           items=items ,
                                           date=date)


        '''
    
    def test_check_if_duplicate_item_id(self):
        user_id=1
        meal_id=1
        items=[ItemDto(
          item_id= 1,
          item_type="dosa",
          quantity= 1
        ),
        ItemDto(
          item_id= 1,
          item_type="dosa",
          quantity= 1
        )]
        date="22-12-1996"
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = PreferenceInteractor(storage)
        presenter.raise_exception_for_duplicate_item.side_effect=BadRequest
        
        with pytest.raises(BadRequest):
            interactor.preference_wrapper(user_id=user_id,
                                          meal_id=meal_id,
                                          items=items,
                                          date=date,
                                          presenter=presenter)
                                          
        
        call_obj=presenter.raise_exception_for_duplicate_item.call_args
        
        error_object=call_obj.args[0]
        
        assert error_object.duplicate_items == [1]
        

class NotFound(Exception):
    pass

class BadRequest(Exception):
    pass

