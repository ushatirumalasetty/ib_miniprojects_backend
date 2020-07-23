# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "user_log_in"
REQUEST_METHOD = "post"
URL_SUFFIX = "user/login/v1/"

from .test_case_01 import TestCase01UserLogInAPITestCase

__all__ = [
    "TestCase01UserLogInAPITestCase"
]
