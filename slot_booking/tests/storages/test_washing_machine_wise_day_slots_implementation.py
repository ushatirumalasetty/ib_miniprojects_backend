import pytest

from slot_booking.constants.enums import Days
from slot_booking.storages.get_washing_machine_wise_day_slots_implementation\
import StorageImplementation
from datetime import time
from slot_booking.interactors.storages.dtos import *

@pytest.mark.django_db
def test_washing_machine_wise_day_slots_implementation(create_washing_machines,create_washing_machine_slots):
    day = Days.SUNDAY.value
    washing_machine_id = "wm1"
    expected_washing_machine_wise_day_slots_dto= [WashingMachineWiseSlotDto(
                 start_time="05:00",
                 end_time="06:00")]
    sql_storage = StorageImplementation()

    washing_machine_wise_day_slots_dto = sql_storage.\
    get_washing_machine_wise_day_wise_slots(day=day,
                                        washing_machine_id=washing_machine_id)

    assert washing_machine_wise_day_slots_dto == \
           expected_washing_machine_wise_day_slots_dto

