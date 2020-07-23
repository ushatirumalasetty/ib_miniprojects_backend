import pytest

from slot_booking.exceptions.exceptions import InvalidWashingMachineId
from slot_booking.storages.get_washing_machine_wise_day_slots_implementation\
import StorageImplementation


@pytest.mark.django_db
def test_validate_washing_machine_id_given_invalid_washing_machine_id_raises_exception():
    washing_machine_id = 10
    sql_storage = StorageImplementation()

    with pytest.raises(InvalidWashingMachineId):
        sql_storage.validate_washing_machine_id(washing_machine_id=washing_machine_id)
