import pytest

from slot_booking.constants.enums import Days
from slot_booking.storages.get_upcomming_slots_implementation\
import StorageImplementation
from datetime import time,date
from slot_booking.interactors.storages.dtos import *

@pytest.mark.django_db
def test_washing_machine_wise_day_slots_implementation(create_users,create_washing_machines,
create_washing_machine_slots,create_user_slots):
    user_id=1
    expected_upcomming_slots_dto_list= [PreviousOrUpcommingSlotsDto(
                 start_time="07:00",
                 end_time="08:00",
                 washing_machine_id=1,
                 date="11-Nov-2020")]

    sql_storage = StorageImplementation()

    upcomming_slots_dto_list = sql_storage.\
    get_upcomming_slots(user_id=user_id)

    assert upcomming_slots_dto_list == \
           expected_upcomming_slots_dto_list
