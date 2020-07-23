# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "list_of_upcomming_slots"
REQUEST_METHOD = "get"
URL_SUFFIX = "upcomming/slots/v1/"

from .test_case_01 import TestCase01ListOfUpcommingSlotsAPITestCase

__all__ = [
    "TestCase01ListOfUpcommingSlotsAPITestCase"
]
