from slot_booking.interactors.storages.update_washing_machine_slots_interface\
import StorageInterface
from slot_booking.interactors.presenters.presenter_interface import\
PresenterInterface
from slot_booking.constants.enums import *
from slot_booking.exceptions.exceptions import *


class UpdateWashingMachineWiseDaySlotsInteractor:
    def __init__(self, storage: StorageInterface,presenter: PresenterInterface):
        self.storage = storage
        self.presenter=presenter
        
        
        
    

    def update_washing_machine_wise_day_wise_slots(self,
                                                day:Days,
                                                washing_machine_id:str,
                                                old_start_time,
                                                old_end_time,
                                                new_start_time,
                                                new_end_time):   
        try:
            self.storage.validate_washing_machine_id(washing_machine_id=washing_machine_id)
        except InvalidWashingMachineId:
            self.presenter.raise_exception_for_invalid_washing_machine_id()
            return

        try:
            self.storage.validate_day(day=day)
        except InvalidDay:
            self.presenter.raise_exception_for_invalid_day()
            return

        try:
            self.storage.\
            check_if_start_time_less_than_end_time(start_time=old_start_time,end_time=old_end_time)
        except:
            self.presenter.raise_exception_start_time_is_not_less_than_end_time()

        try:
            self.storage.\
            check_if_start_time_less_than_end_time(start_time=new_start_time,end_time=new_end_time)
        except:
            self.presenter.raise_exception_start_time_is_not_less_than_end_time()

        
        self.storage.update_washing_machine_wise_day_wise_slots(day=day,
                                                washing_machine_id=washing_machine_id,
                                                old_start_time=old_start_time,
                                                old_end_time=old_end_time,
                                                new_start_time=new_start_time,
                                                new_end_time=new_end_time)
