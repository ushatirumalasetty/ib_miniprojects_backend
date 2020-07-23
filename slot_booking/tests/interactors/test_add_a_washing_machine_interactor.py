from unittest.mock import create_autospec

from slot_booking.interactors.\
    add_a_washing_machine_interactor import *
from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface
from slot_booking.interactors.storages.\
add_a_washing_machine_interface import StorageInterface
from slot_booking.interactors.storages.dtos import *
from datetime import date,time
import pytest
from slot_booking.exceptions.exceptions import *
from slot_booking.constants.enums import WashingMachineStatus

class TestAddAWashingMachineInteractor:

    def test_add_a_washing_machine_interactor(self):
        washing_machine_id = "wm1"
        status = WashingMachineStatus.ACTIVE.value
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = AddAWashingMachineInteractor(storage=storage,
                                                presenter=presenter)
       
        interactor.add_a_washing_machine_interactor(
                                        washing_machine_id=washing_machine_id,
                                        status=status)
                                                
        storage.add_a_washing_machine.assert_called_once_with(
                                        washing_machine_id=washing_machine_id,
                                        status=status)
                                        
                                                
    def test_given_washing_machine_id_already_exists_raises_exception(self):
            washing_machine_id = "wm1"
            status = WashingMachineStatus.ACTIVE.value
            storage = create_autospec(StorageInterface)
            presenter = create_autospec(PresenterInterface)
            interactor = AddAWashingMachineInteractor(storage=storage,
                                                presenter=presenter)
            storage.check_if_washing_machine_id_exits.side_effect = WashingMachineAlreadyExists
            presenter.raise_exception_for_invalid_washing_machine_id.side_effect = NotFound
    
            with pytest.raises(NotFound):
                interactor.add_washing_machine_wise_day_wise_slots_interactor(day=day,
                                        washing_machine_id=washing_machine_id,
                                        start_time=start_time,
                                        end_time=end_time)
        
            storage.validate_washing_machine_id.\
            assert_called_once_with(washing_machine_id=washing_machine_id)
            presenter.raise_exception_for_invalid_washing_machine_id.assert_called_once()

    
    def test_given_invalid_day_raises_exception(self):
        washing_machine_id = "wm1"
        day="USHA"
        start_time = '8:00'
        end_time='9:00'
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = AddWashingMachineWiseDaySlotsInteractor(storage, presenter)
        storage.validate_day.side_effect = InvalidDay
        presenter.raise_exception_for_invalid_day.side_effect = NotFound

        with pytest.raises(NotFound):
            interactor.add_washing_machine_wise_day_wise_slots_interactor(day=day,
                                        washing_machine_id=washing_machine_id,
                                        start_time=start_time,
                                        end_time=end_time)
        
        storage.validate_day.\
        assert_called_once_with(day=day)
        presenter.raise_exception_for_invalid_day.assert_called_once()
    
    def test_check_if_start_time_less_than_end_time(self):
        washing_machine_id = "wm1"
        day=Days.SUNDAY.value
        start_time = '10:00'
        end_time='9:00'
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = AddWashingMachineWiseDaySlotsInteractor(storage, presenter)
        storage.check_if_start_time_less_than_end_time.\
        side_effect = StartTimeGreaterThanEndTimeError
        presenter.raise_exception_start_time_is_not_less_than_end_time.side_effect = NotFound
        with pytest.raises(NotFound):
            interactor.add_washing_machine_wise_day_wise_slots_interactor(day=day,
                                        washing_machine_id=washing_machine_id,
                                        start_time=start_time,
                                        end_time=end_time)
        storage.check_if_start_time_less_than_end_time.\
        assert_called_once_with(start_time=start_time, end_time=end_time)
        presenter.raise_exception_start_time_is_not_less_than_end_time\
        .assert_called_once()
