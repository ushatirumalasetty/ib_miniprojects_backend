"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from slot_booking.tests.factory.fact import UserFactory, WashingMachineFactory,\
WashingMachineSlotFactory, UserSlotFactory

REQUEST_BODY = """
{
    "user_id": 1
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["read", "write"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}
    



class TestCase01ListOfPreviousSlotsAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE
    
    
    def setupUser(self, username, password):
        super(TestCase01ListOfPreviousSlotsAPITestCase, self).setupUser(
            username=username, password=password
        )
        
    user_obj = UserFactory.create_batch(1, username="261ada3c118d1")
    print("*"*100)
    washing_machine_obj = WashingMachineFactory.create_batch(1)
    print("*"*100)
    washing_machine_slot_obj = WashingMachineSlotFactory.create_batch(1, washing_machine=washing_machine_obj[0])
    print("*"*100)
    user_slot_obj = UserSlotFactory.create_batch(1, washing_machine_slot=washing_machine_slot_obj[0], user=user_obj[0])
    print("*"*100)

    def test_case(self):
        response = self.default_test_case() 
        
        self.assert_match_snapshot(
            name='list_of_previous_slots',
            value=response
        )
