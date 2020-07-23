import pytest

from slot_booking.constants.enums import Days
from slot_booking.storages.update_washing_machine_slot_implementation\
import StorageImplementation
from datetime import time
from slot_booking.interactors.storages.dtos import *
from slot_booking.models.user import *

@pytest.mark.django_db
def test_update_washing_machine_wise_day_wise_slots(create_washing_machines,create_washing_machine_slots):
    day = Days.SUNDAY.value
    washing_machine_id = "wm1"
    old_start_time = time(5)
    old_end_time = time(6)
    new_start_time = time(2)
    new_end_time = time(3)
    
    sql_storage = StorageImplementation()

    sql_storage.update_washing_machine_wise_day_wise_slots(day=day,
                                                     washing_machine_id=washing_machine_id,
                                                     old_start_time=old_start_time,
                                                     old_end_time=old_end_time,
                                                     new_start_time=new_start_time,
                                                     new_end_time=new_end_time)
    
    washing_machine_obj = WashingMachine.objects.get(washing_machine_id=washing_machine_id)    
    washing_machine_slot_obj = WashingMachineSlot.objects.get(day=day,
                                    washing_machine=washing_machine_obj,
                                    start_time=new_start_time,
                                    end_time=new_end_time)
                                    
    assert washing_machine_slot_obj.start_time == new_start_time
    assert washing_machine_slot_obj.end_time == new_end_time
    