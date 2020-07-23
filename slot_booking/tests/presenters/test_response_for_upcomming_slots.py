from slot_booking.constants.enums import *
from slot_booking.interactors.storages.dtos import \
    PreviousOrUpcommingSlotsDto
from slot_booking.presenters.presenter_implementation import PresenterImplementation
from datetime import date

def test_get_response_for_upcomming_slots():
    upcomming_slots_dtos_list= [PreviousOrUpcommingSlotsDto(
                 start_time="05:00",
                 end_time="06:00",
                 washing_machine_id=1,
                 date="11-Nov-2020")]

    json_presenter = PresenterImplementation()
    expected_upcomming_slots_list = [
        {
            "start_time": "05:00",
            "end_time": "06:00",
            "washing_machine_id": 1,
            "date": "11-Nov-2020"
        }
    ]

    actual_upcomming_slots_list = json_presenter.get_reponse_for_upcomming_slots_list(
        upcomming_slots_list=upcomming_slots_dtos_list
    )

    assert actual_upcomming_slots_list == expected_upcomming_slots_list
