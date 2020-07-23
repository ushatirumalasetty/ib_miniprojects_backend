# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "update_slots_of_washing_machine_on_a_day"
REQUEST_METHOD = "post"
URL_SUFFIX = "update/washing_machine_slots/v1/"

from .test_case_01 import TestCase01UpdateSlotsOfWashingMachineOnADayAPITestCase

__all__ = [
    "TestCase01UpdateSlotsOfWashingMachineOnADayAPITestCase"
]
