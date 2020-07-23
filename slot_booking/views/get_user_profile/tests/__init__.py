# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "get_user_profile"
REQUEST_METHOD = "get"
URL_SUFFIX = "get/user_profile/v1/"

from .test_case_01 import TestCase01GetUserProfileAPITestCase

__all__ = [
    "TestCase01GetUserProfileAPITestCase"
]
