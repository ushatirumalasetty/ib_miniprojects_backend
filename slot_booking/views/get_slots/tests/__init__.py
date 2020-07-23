# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "get_slots"
REQUEST_METHOD = "get"
URL_SUFFIX = "get/slots/v1/"

from .test_case_01 import TestCase01GetSlotsAPITestCase

__all__ = [
    "TestCase01GetSlotsAPITestCase"
]
