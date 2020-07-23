import pytest

from slot_booking.constants.enums import Days
from slot_booking.storages.add_washing_machine_wise_day_slots_implementation\
import StorageImplementation
from datetime import time
from slot_booking.interactors.storages.dtos import *
from slot_booking.models.user import *

@pytest.mark.django_db
def test_add_washing_machine_wise_day_slots_implementation(create_washing_machines):
    day = Days.SUNDAY.value
    washing_machine_id = "wm1"
    start_time = time(2)
    end_time = time(3)
    sql_storage = StorageImplementation()

    sql_storage.add_washing_machine_wise_day_wise_slots(day=day,
                                        washing_machine_id=washing_machine_id,
                                        start_time=start_time,
                                        end_time=end_time)
    
    washing_machine_obj = WashingMachine.objects.get(washing_machine_id=washing_machine_id)    
    washing_machine_slot_obj = WashingMachineSlot.objects.get(day=day,
                                    washing_machine=washing_machine_obj,
                                    start_time=start_time,
                                    end_time=end_time)
    assert washing_machine_slot_obj.start_time == start_time
    assert washing_machine_slot_obj.end_time == end_time
    