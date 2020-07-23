# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "add_a_washing_machine"
REQUEST_METHOD = "post"
URL_SUFFIX = "add/washing_machine/v1/"

from .test_case_01 import TestCase01AddAWashingMachineAPITestCase

__all__ = [
    "TestCase01AddAWashingMachineAPITestCase"
]
