# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "slots_of_washing_machine_on_a_day"
REQUEST_METHOD = "get"
URL_SUFFIX = "get/washing_machine_slots/v1/"

from .test_case_01 import TestCase01SlotsOfWashingMachineOnADayAPITestCase

__all__ = [
    "TestCase01SlotsOfWashingMachineOnADayAPITestCase"
]
