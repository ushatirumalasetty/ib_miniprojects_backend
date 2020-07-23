from abc import ABC
from abc import abstractmethod
import datetime
from slot_booking.constants.enums import *
from typing import List
from .dtos import *

class StorageInterface(ABC):
    
    
    @abstractmethod
    def get_slots_for_particular_days_with_avilablity_status(self):
        pass

'''
    @abstractmethod
    def validate_user_name(self, user_name:str):
        pass

    @abstractmethod
    def validate_password(self, user_name:str, password:str):
        pass

    @abstractmethod
    def check_if_confirm_password_match_password(self,
                                                 user_name:str,
                                                 password:str,
                                                 confirm_password:str):
        pass

    @abstractmethod
    def user_signup(self, username:str, password:str, confirm_password:str):
        pass

    @abstractmethod
    def user_login(self, username:str, password:str):
        pass

    @abstractmethod
    def get_slots_for_particular_days_with_avilablity_status(self):
        pass


    @abstractmethod
    def get_list_of_datewise_slots_till_range(self, user_id:int):
        pass

    
    
    @abstractmethod
    def add_washing_machine_wise_day_wise_slots(self, day:Days, washing_machine_id:str):
        pass
    
    @abstractmethod
    def view_user_profile(self):
        pass

    @abstractmethod
    def update_user_profile(self):
        pass

    @abstractmethod
    def change_user_profile_password(self):
        pass

    @abstractmethod
    def register_washing_machine_with_its_id(self, washing_machine_id: int):
        pass

    @abstractmethod
    def add_a_time_slot_for_a_specific_day(self,
                                           date: datetime.date, slot_start_time: datetime.time):
        pass

    @abstractmethod
    def update_a_time_slot_for_a_specific_day(self):
        pass

    @abstractmethod
    def check_for_the_previous_booking_of_the_user(self):
        pass

    @abstractmethod
    def verify_time_gap_of_days_required_before_booking_other_slot(self):
        pass

    @abstractmethod
    def verify_time_gap_of_days_till_which_user_can_book_a_slot(self):
        pass

    @abstractmethod
    def cancel_a_slot(self):
        pass

    @abstractmethod
    def verify_time_gap_required_of_hours_before_cancelling_the_slot(self):
        pass

    @abstractmethod
    def turn_washing_machine_active_or_inactive(self):
        pass

    @abstractmethod
    def get_pending_and_resolved_issues_list(self):
        pass

    @abstractmethod
    def mark_pending_issues_as_resolved(self):
        pass

    @abstractmethod
    def mark_washing_machine_slot_unused(self):
        pass


    @abstractmethod
    def get_upcomming_slots_list(self):
        pass

    @abstractmethod
    def check_details_of_a_preson_booked_on_a_particular_slot(self):
        pass

    @abstractmethod
    def request_an_user_asking_for_his_slot(self):
        pass

    @abstractmethod
    def get_requests_list_of_an_user(self):
        pass

    @abstractmethod
    def respond_to_request(self):
        pass

    @abstractmethod
    def report_an_issue(self):
        pass


    @abstractmethod
    def check_no_of_times_had_unused_the_slot(self):
        pass
'''