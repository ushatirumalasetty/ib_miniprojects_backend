# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "book_a_slot"
REQUEST_METHOD = "post"
URL_SUFFIX = "book/slot/v1/"

from .test_case_01 import TestCase01BookASlotAPITestCase

__all__ = [
    "TestCase01BookASlotAPITestCase"
]
