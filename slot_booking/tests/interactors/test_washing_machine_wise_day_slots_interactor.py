from unittest.mock import create_autospec
from slot_booking.constants.enums import *
from slot_booking.interactors.\
    get_washing_machine_wise_day_slots_interactor import *
from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface
from slot_booking.interactors.\
storages.get_washing_machine_wise_storage_interface import *
from slot_booking.interactors.storages.dtos import *
from datetime import date,time
from slot_booking.exceptions.exceptions import *
import pytest

class TestGetWashingMachineWiseDaySlotsInteractor:


    def test_given_invalid_washing_machine_id_raises_exception(self):
        
        washing_machine_id = "wm10"
        day=Days.SUNDAY.value
        limit=10
        offset=10
        
        storage = create_autospec(StorageInterface)
        
        presenter = create_autospec(PresenterInterface)
        
        interactor = GetWashingMachineWiseDaySlotsInteractor(storage)
        
        storage.\
        validate_washing_machine_id.side_effect = InvalidWashingMachineId
        
        presenter.\
        raise_exception_for_invalid_washing_machine_id.side_effect = NotFound

        with pytest.raises(NotFound):
            interactor.get_washing_machine_wise_day_wise_slots_wrapper(day=day,
                                      washing_machine_id=washing_machine_id,
                                      limit=limit,
                                      offset=offset,
                                      presenter=presenter)

        storage.validate_washing_machine_id.\
        assert_called_once_with(washing_machine_id=washing_machine_id)
        
        presenter.\
        raise_exception_for_invalid_washing_machine_id.assert_called_once()


    def test_given_day_doesnt_belong_to_washing_machine(self):
        
        washing_machine_id = "wm10"
        day="FRIDAY"
        limit=10
        offset=10
        
        storage = create_autospec(StorageInterface)
        
        presenter = create_autospec(PresenterInterface)
        
        interactor = GetWashingMachineWiseDaySlotsInteractor(storage)
        
        storage.validate_if_day_belong_to_washing_machine.\
        side_effect = DayDoesntBelongToWashingMachine
        
        presenter.raise_exception_for_day_doesnt_belong_to_washing_machine.\
        side_effect = NotFound

        with pytest.raises(NotFound):
            interactor.get_washing_machine_wise_day_wise_slots_wrapper(day=day,
                                      washing_machine_id=washing_machine_id,
                                      limit=limit,
                                      offset=offset,
                                      presenter=presenter)

        storage.validate_if_day_belong_to_washing_machine.\
        assert_called_once_with(washing_machine_id=washing_machine_id,day=day)

        presenter.raise_exception_for_day_doesnt_belong_to_washing_machine\
        .assert_called_once()


    def test_given_invalid_day_raises_exception(self):
        
        washing_machine_id = "wm1"
        day="USHA"
        limit=10
        offset=10
        
        storage = create_autospec(StorageInterface)
        
        presenter = create_autospec(PresenterInterface)
        
        interactor = GetWashingMachineWiseDaySlotsInteractor(storage)
        
        presenter.raise_exception_for_invalid_day.side_effect = NotFound
        
        with pytest.raises(NotFound):
            interactor.get_washing_machine_wise_day_wise_slots_wrapper(day=day,
                                      washing_machine_id=washing_machine_id,
                                      limit=limit,
                                      offset=offset,
                                      presenter=presenter)

        call_obj = presenter.raise_exception_for_invalid_day.call_args
        
        error_object = call_obj.args
        
        assert error_object == ()
    

    def test_washing_wise_day_slots_given_valid_details(self):
        
        washing_machine_id = "wm1"
        day=Days.SUNDAY.value
        limit=10
        offset=10
        
        storage = create_autospec(StorageInterface)
        
        presenter = create_autospec(PresenterInterface)
        
        interactor = GetWashingMachineWiseDaySlotsInteractor(storage)
        
        expected_output = slots_dto_list = [
            {
                "start_time": time(8),
                "end_time": time(9)

            },
            {
                "start_time": time(9),
                "end_time": time(10)

            }
        ]
        
        slots_dto = [
            WashingMachineWiseSlotDto(
                start_time=time(8),
                end_time=time(9)),
            WashingMachineWiseSlotDto(
                start_time=time(9),
                end_time=time(10))
        ]
        
        storage.get_washing_machine_wise_day_wise_slots.return_value = slots_dto
        
        presenter.get_response_washing_machine_wise_day_wise_slots.return_value \
            = expected_output

        actual_result = interactor.\
        get_washing_machine_wise_day_wise_slots_response(limit=limit,
                    washing_machine_id=washing_machine_id,
                    day=day,
                    offset=offset,
                    presenter=presenter)

        assert actual_result == expected_output

