from slot_booking.interactors.storages.add_washing_machine_wise_storage_interface \
import StorageInterface
from slot_booking.interactors.presenters.presenter_interface import\
PresenterInterface
from slot_booking.constants.enums import *
from slot_booking.exceptions.exceptions import *


class AddWashingMachineWiseDaySlotsInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage
        
        
    def  add_washing_machine_wise_day_wise_slots_interactor_wrapper(self, day:Days,
                                                washing_machine_id:str,
                                                start_time,
                                                end_time,
                                                presenter:PresenterInterface):
        try:
            self.add_washing_machine_wise_day_wise_slots_interactor(day=day,
                                        washing_machine_id=washing_machine_id,
                                        start_time=start_time,
                                        end_time=end_time)
        except InvalidWashingMachineId:
            presenter.raise_exception_for_invalid_washing_machine_id()
        except InvalidDay:
            presenter.raise_exception_for_invalid_day()
        except StartTimeGreaterThanEndTimeError:
            presenter.raise_exception_start_time_is_not_less_than_end_time()

        

    def add_washing_machine_wise_day_wise_slots_interactor(self, day:Days,
                                                washing_machine_id:str,
                                                start_time,
                                                end_time):
        self.storage.\
            validate_washing_machine_id(washing_machine_id=washing_machine_id)
        self.storage.validate_day(day=day)
        self.storage.\
            check_if_start_time_less_than_end_time(start_time=start_time,
                                                   end_time=end_time)
        self.storage.add_washing_machine_wise_day_wise_slots(
                                        day=day,
                                        washing_machine_id=washing_machine_id,
                                        start_time=start_time,
                                        end_time=end_time)
        