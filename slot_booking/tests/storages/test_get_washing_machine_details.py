import pytest

from slot_booking.constants.enums import Days
from slot_booking.storages.get_washing_machines_details_implementation\
import StorageImplementation
from datetime import time,date
from slot_booking.interactors.storages.dtos import *

@pytest.mark.django_db
def test_washing_machine_wise_day_slots_implementation(create_washing_machines):
    expected_washing_machines_details_dto_list= [WashingMachineDto(
                 washing_machine_id="wm1",
                 status="ACTIVE"),
            WashingMachineDto(
                 washing_machine_id="wm2",
                 status="INACTIVE")
                 ]

    sql_storage = StorageImplementation()

    washing_machines_details_dto_list = sql_storage.\
    get_washing_machines_details()
    print(washing_machines_details_dto_list)

    assert washing_machines_details_dto_list == \
           expected_washing_machines_details_dto_list
