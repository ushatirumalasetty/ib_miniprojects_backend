# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "get_washing_machines_details"
REQUEST_METHOD = "get"
URL_SUFFIX = "get/washing_machines_details/v1/"

from .test_case_01 import TestCase01GetWashingMachinesDetailsAPITestCase

__all__ = [
    "TestCase01GetWashingMachinesDetailsAPITestCase"
]
