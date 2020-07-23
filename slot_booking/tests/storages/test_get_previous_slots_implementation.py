import pytest

from slot_booking.constants.enums import Days
from slot_booking.storages.get_previous_slots_implementation\
import StorageImplementation
from datetime import time,date
from slot_booking.interactors.storages.dtos import *

@pytest.mark.django_db
def test_previous_slots_implementation(create_users,create_washing_machines,
create_washing_machine_slots,create_user_slots):
    user_id=1
    expected_previous_slots_dto_list= [PreviousOrUpcommingSlotsDto(
                 start_time="05:00",
                 end_time="06:00",
                 washing_machine_id=1,
                 date="01-Jan-2020")]

    sql_storage = StorageImplementation()

    previous_slots_dto_list = sql_storage.\
    get_previous_slots(user_id=user_id)

    assert previous_slots_dto_list == \
           expected_previous_slots_