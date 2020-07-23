from slot_booking.constants.enums import *
from slot_booking.interactors.storages.dtos import \
    WashingMachineDto
from slot_booking.presenters.presenter_implementation import PresenterImplementation
from datetime import date

def test_get_response_for_washing_machines_details():
    washing_machines_details_dtos_list= [WashingMachineDto(
                 washing_machine_id="wm1",
                 status="ACTIVE"),
            WashingMachineDto(
                 washing_machine_id="wm2",
                 status="INACTIVE"),
                 ]

    json_presenter = PresenterImplementation()
    expected_washing_machines_details_list = [
        {
            "washing_machine_id":"wm1",
            "status":"ACTIVE"
        },
        {
            "washing_machine_id":"wm2",
            "status":"INACTIVE"
        }
    ]

    actual_washing_machines_details_list = json_presenter.get_response_for_washing_machines_details(
        washing_machines_details_dtos_list=washing_machines_details_dtos_list
    )

    assert actual_washing_machines_details_list == expected_washing_machines_details_list
