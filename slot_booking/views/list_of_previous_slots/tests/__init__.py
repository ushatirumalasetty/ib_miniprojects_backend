# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "list_of_previous_slots"
REQUEST_METHOD = "get"
URL_SUFFIX = "previous/slots/v1/"

from .test_case_01 import TestCase01ListOfPreviousSlotsAPITestCase

__all__ = [
    "TestCase01ListOfPreviousSlotsAPITestCase"
]
