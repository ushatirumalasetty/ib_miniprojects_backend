from unittest.mock import create_autospec

from slot_booking.interactors.\
    get_avilable_slots_interactor import \
    GetAvilableSlotsInteractor
from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface
from slot_booking.interactors.storages.storage_interface import \
    StorageInterface
from slot_booking.interactors.storages.dtos import *

class TestGetAvilableSlotsInteractor:
    def test_returns_avilable_slots(self):
        user_id = 1
        datewise_slots_response=[]
        expected_list =datewise_slots_response
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetAvilableSlotsInteractor(storage, presenter)
        storage.get_slots_for_particular_days_with_avilablity_status.\
            return_value = datewise_slots_response
        presenter.get_response_of_list_of_datewise_slots_till_range. \
            return_value = expected_list

        actual_list = interactor.get_slots_for_particular_days_with_avilablity_status(user_id=user_id)

        assert expected_list == actual_list
        presenter.get_response_of_list_of_datewise_slots_till_range. \
            assert_called_once_with(list_of_datewise_slots=actual_list)
        storage.get_slots_for_particular_days_with_avilablity_status. \
            assert_called_once()
