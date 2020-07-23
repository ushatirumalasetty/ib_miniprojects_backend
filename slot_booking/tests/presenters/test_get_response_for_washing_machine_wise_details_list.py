from slot_booking.constants.enums import *
from slot_booking.interactors.storages.dtos import \
    WashingMachineWiseSlotDto
from slot_booking.presenters.presenter_implementation import PresenterImplementation
from datetime import date

def test_get_response_for_washing_machine_wise_day_slots():
    washing_machine_wise_day_slots_dto_list= [WashingMachineWiseSlotDto(
                 start_time="05:00",
                 end_time="06:00")]

    json_presenter = PresenterImplementation()
    expected_washing_machine_wise_day_slots_list = [
        {
            "start_time":"05:00",
            "end_time":"06:00"
        }

    ]

    actual_washing_machine_wise_day_slots_list = json_presenter.\
    get_response_washing_machine_wise_day_wise_slots(
        slots_dto_list=washing_machine_wise_day_slots_dto_list
    )
    
    assert actual_washing_machine_wise_day_slots_list == expected_washing_machine_wise_day_slots_list
