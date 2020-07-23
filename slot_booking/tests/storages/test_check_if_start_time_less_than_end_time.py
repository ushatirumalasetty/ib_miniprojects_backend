import pytest

from slot_booking.exceptions.exceptions import StartTimeGreaterThanEndTimeError
from slot_booking.storages.add_washing_machine_wise_day_slots_implementation\
import StorageImplementation


@pytest.mark.django_db
def test_check_if_start_time_less_than_end_time():
    start_time = "3:00"
    end_time = "2:00"
    sql_storage = StorageImplementation()

    with pytest.raises(StartTimeGreaterThanEndTimeError):
        sql_storage.check_if_start_time_less_than_end_time(start_time=start_time,
        end_time=end_time)
