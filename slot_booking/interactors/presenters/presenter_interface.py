from abc import ABC
from abc import abstractmethod
from slot_booking.constants.enums import *
from typing import List
from slot_booking.interactors.storages.dtos import *


class PresenterInterface(ABC):
    @abstractmethod
    def raise_exception_for_invalid_username(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_password(self):
        pass

    @abstractmethod
    def raise_exception_for_password_didnt_match(self):
        pass

class AvilableSlots(ABC):
    
    @abstractmethod
    def get_response_of_list_of_datewise_slots_till_range(self,
        avilable_slots:DatewiseSlotStatusListDto):
        pass
    
class PreviousSlotsInterface(ABC):

    @abstractmethod
    def get_reponse_for_previous_slots_list(self,
        previous_slots_list:PreviousOrUpcommingSlotsDtoList):
        pass

class UpcommingSlotsInterface(ABC):

    @abstractmethod
    def get_reponse_for_upcomming_slots_list(self,
        upcomming_slots_list:PreviousOrUpcommingSlotsDtoList):
        pass

class DatewiseSlotInterface(ABC):

    @abstractmethod
    def get_response_washing_machine_wise_day_wise_slots(self,
        slots_dto_list:ListWashingMachineWiseSlotDto):
        pass

    @abstractmethod
    def raise_exception_for_invalid_washing_machine_id(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_day(self):
        pass

    @abstractmethod
    def raise_exception_for_day_doesnt_belong_to_washing_machine(self):
        pass

    @abstractmethod
    def raise_exception_start_time_is_not_less_than_end_time(self):
        pass




class GetWashingMachineDetailsInterface(ABC):

    @abstractmethod
    def get_response_for_washing_machines_details(self,
    washing_machines_details_dtos_list:List[WashingMachineDto]):
        pass
    
    
    
    @abstractmethod
    def raise_washing_machine_already_exist(self):
        pass
    
    @abstractmethod
    def raise_exception_for_invalid_washing_machine_status(self):
        pass
    
    @abstractmethod
    def get_response_for_get_requests_details_of_an_user(self,
            requests_details_list: List[RequestCompleteDetailsDto]):
        pass

    @abstractmethod
    def get_token_response_dto(self, tokens_dto, user_login_dto):
        pass
    
