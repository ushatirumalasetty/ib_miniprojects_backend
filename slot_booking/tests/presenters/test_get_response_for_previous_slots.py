from slot_booking.constants.enums import *
from slot_booking.interactors.storages.dtos import \
    PreviousOrUpcommingSlotsDto
from slot_booking.presenters.presenter_implementation import PresenterImplementation
from datetime import date

def test_get_response_for_previous_slots():
    previous_slots_dto_list= [PreviousOrUpcommingSlotsDto(
                 start_time="05:00",
                 end_time="06:00",
                 washing_machine_id=1,
                 date="01-Jan-2020")]

    json_presenter = PresenterImplementation()
    expected_previous_slots_list = [
        {
            "start_time": "05:00",
            "end_time": "06:00",
            "washing_machine_id": 1,
            "date": "01-Jan-2020"
        }
    ]

    actual_previous_slots_list = json_presenter.get_reponse_for_previous_slots_list(
        previous_slots_list=previous_slots_dto_list
    )

    assert actual_previous_slots_list == expected_previous_slots_list
