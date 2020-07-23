import pytest

from slot_booking.exceptions.exceptions import InvalidDay
from slot_booking.storages.get_washing_machine_wise_day_slots_implementation\
import StorageImplementation


@pytest.mark.django_db
def test_validate_day_for_invalid_day():
    day = "usha"
    sql_storage = StorageImplementation()

    with pytest.raises(InvalidDay):
        sql_storage.validate_day(day=day)
