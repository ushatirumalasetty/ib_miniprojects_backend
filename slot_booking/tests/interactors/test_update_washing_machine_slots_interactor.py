from unittest.mock import create_autospec
from slot_booking.constants.enums import *
from slot_booking.interactors.\
    update_washing_machine_slots_interactor import *
from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface
from slot_booking.interactors.\
storages.update_washing_machine_slots_interface import *
from slot_booking.interactors.storages.dtos import *
from datetime import date,time
from slot_booking.exceptions.exceptions import *
import pytest

class TestUpdateWashingMachineWiseDaySlotsInteractor:
    
    
    def test_update_washing_machine_wise_day_wise_slots(self):
        washing_machine_id = "wm1"
        day=Days.SUNDAY.value
        old_start_time = '8:00'
        old_end_time='9:00'
        new_start_time= '11:00'
        new_end_time = '12:00'
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = UpdateWashingMachineWiseDaySlotsInteractor(storage=storage,
                                                presenter=presenter)

        interactor.update_washing_machine_wise_day_wise_slots(day=day,
                                        washing_machine_id=washing_machine_id,
                                        old_start_time=old_start_time,
                                        old_end_time=old_end_time,
                                        new_start_time=new_start_time,
                                        new_end_time=new_end_time)

        storage.update_washing_machine_wise_day_wise_slots.assert_called_once_with(day=day,
                                        washing_machine_id=washing_machine_id,
                                        old_start_time=old_start_time,
                                        old_end_time=old_end_time,
                                        new_start_time=new_start_time,
                                        new_end_time=new_end_time)


    def test_given_invalid_washing_machine_id_raises_exception(self):
        washing_machine_id = "chjgwm1"
        day=Days.SUNDAY.value
        old_start_time = '8:00'
        old_end_time='9:00'
        new_start_time= '11:00'
        new_end_time = '12:00'
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = UpdateWashingMachineWiseDaySlotsInteractor(storage=storage,
                                                presenter=presenter)

        storage.validate_washing_machine_id.side_effect = InvalidWashingMachineId
        presenter.raise_exception_for_invalid_washing_machine_id.side_effect = NotFound

        with pytest.raises(NotFound):
            interactor.update_washing_machine_wise_day_wise_slots(day=day,
                                        washing_machine_id=washing_machine_id,
                                        old_start_time=old_start_time,
                                        old_end_time=old_end_time,
                                        new_start_time=new_start_time,
                                        new_end_time=new_end_time)

        storage.validate_washing_machine_id.\
        assert_called_once_with(washing_machine_id=washing_machine_id)
        presenter.raise_exception_for_invalid_washing_machine_id.assert_called_once()

    def test_given_invalid_day_raises_exception(self):
        washing_machine_id = "wm1"
        day="usha"
        old_start_time = '8:00'
        old_end_time='9:00'
        new_start_time= '11:00'
        new_end_time = '12:00'
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = UpdateWashingMachineWiseDaySlotsInteractor(storage=storage,
                                                presenter=presenter)
        storage.validate_day.side_effect = InvalidDay
        presenter.raise_exception_for_invalid_day.side_effect = NotFound

        with pytest.raises(NotFound):
            interactor.update_washing_machine_wise_day_wise_slots(day=day,
                                        washing_machine_id=washing_machine_id,
                                        old_start_time=old_start_time,
                                        old_end_time=old_end_time,
                                        new_start_time=new_start_time,
                                        new_end_time=new_end_time)
        storage.validate_day.\
        assert_called_once_with(day=day)
        presenter.raise_exception_for_invalid_day.assert_called_once()

    def test_check_if_start_time_less_than_end_time(self):
        washing_machine_id = "wm1"
        day=Days.SUNDAY.value
        old_start_time = '10:00'
        old_end_time='9:00'
        new_start_time= '11:00'
        new_end_time = '12:00'
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = UpdateWashingMachineWiseDaySlotsInteractor(storage=storage,
                                                presenter=presenter)
        storage.check_if_start_time_less_than_end_time.\
        side_effect = StartTimeGreaterThanEndTimeError
        presenter.raise_exception_start_time_is_not_less_than_end_time.side_effect = NotFound
        with pytest.raises(NotFound):
            interactor.update_washing_machine_wise_day_wise_slots(day=day,
                                        washing_machine_id=washing_machine_id,
                                        old_start_time=old_start_time,
                                        old_end_time=old_end_time,
                                        new_start_time=new_start_time,
                                        new_end_time=new_end_time)
        storage.check_if_start_time_less_than_end_time.\
        assert_called_once_with(start_time=old_start_time, end_time=old_end_time)
        presenter.raise_exception_start_time_is_not_less_than_end_time\
        .assert_called_once()
    

