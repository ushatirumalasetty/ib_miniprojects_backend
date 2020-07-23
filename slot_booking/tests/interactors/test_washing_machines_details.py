from unittest.mock import create_autospec
from slot_booking.constants.enums import *
from slot_booking.interactors.\
    get_washing_machines_details_interactor import *
from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface
from slot_booking.interactors.\
storages.get_washig_machines_details_interface import *
from slot_booking.interactors.storages.dtos import *
from datetime import date,time


def test_washing_machines_details():
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetWashingMachinesDetailsInteractor(storage, presenter)
        expected_output = washing_machines_details_dtos_list = [
            {
                "washing_machine_id": "wm1",
                "status": "ACTIVE"
            },
            {
                "washing_machine_id": "wm2",
                "status": "INACTIVE"
            }
        ]
        slots_dto = [
            WashingMachineDto(
                washing_machine_id="wm1",
                status="ACTIVE"),
            WashingMachineDto(
                washing_machine_id="wm2",
                status="INACTIVE")
        ]
        storage.get_washing_machines_details.return_value = slots_dto
        presenter.get_response_for_washing_machines_details.return_value \
            = expected_output

        actual_result = interactor.get_washing_machines_details_interactor()

        assert actual_result == expected_output

