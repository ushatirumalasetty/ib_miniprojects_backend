# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "get_requests_of_an_user"
REQUEST_METHOD = "get"
URL_SUFFIX = "get/requests/v1/"

from .test_case_01 import TestCase01GetRequestsOfAnUserAPITestCase

__all__ = [
    "TestCase01GetRequestsOfAnUserAPITestCase"
]
