from unittest.mock import create_autospec

from slot_booking.interactors.\
    get_previous_slot_interactor import *
from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface
from slot_booking.interactors.storages.get_previous_slots_interface import \
    StorageInterface
from slot_booking.interactors.storages.dtos import *
from datetime import date,time


class TestGetPreviousSlotInteractor:

    def test_get_previous_slots_interactor(self):
        user_id = 1
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetPreviousSlotsInteractor(storage=storage,
                                                presenter=presenter)
        expected_output =  previous_slots_list =[
            {
                "start_time": '08:00AM',
                "end_time": '09:00AM',
                "washing_machine_id": "wm1",
                "date": date(2020,12,1)
            },
            {
                "start_time": '09:00AM',
                "end_time": '010:00AM',
                "washing_machine_id": "wm2",
                "date": date(2020,12,2)

            }
        ]
        
        previous_or_upcomming_slots_dto = [
            PreviousOrUpcommingSlotsDto(
                start_time=time(8).strftime("%H:%M%p"),
                end_time=time(9).strftime("%H:%M%p"),
                washing_machine_id="wm1",
                date=date(2020,12,2)),
            PreviousOrUpcommingSlotsDto(
                start_time=time(9).strftime("%H:%M%p"),
                end_time=time(10).strftime("%H:%M%p"),
                washing_machine_id="wm2",
                date=date(2020,12,2))
        ]

        storage.get_previous_slots.return_value = previous_or_upcomming_slots_dto
        presenter.get_reponse_for_previous_slots_list.return_value \
            = expected_output

        actual_result = interactor.get_previous_slots_interactor(
            user_id=user_id
        )

        assert actual_result == expected_output
  