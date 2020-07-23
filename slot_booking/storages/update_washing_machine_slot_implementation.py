from typing import Optional, List
from slot_booking.interactors.storages.update_washing_machine_slots_interface\
import *
from slot_booking.models.user import *
from slot_booking.constants.enums import *
from slot_booking.exceptions.exceptions import *
import datetime
from slot_booking.interactors.storages.dtos import *



class StorageImplementation(StorageInterface):


    def update_washing_machine_wise_day_wise_slots(self,day:Days,
                                                     washing_machine_id:str,
                                                     old_start_time,
                                                     old_end_time,
                                                     new_start_time,
                                                     new_end_time):

        self.validate_washing_machine_id(washing_machine_id)
        self.validate_day(day)
        self.check_if_start_time_less_than_end_time(old_start_time, old_end_time)
        self.check_if_start_time_less_than_end_time(new_start_time, new_end_time)

        WashingMachineSlot.objects.\
        filter(washing_machine__washing_machine_id=washing_machine_id,\
               day=day,
               start_time=old_start_time,
               end_time=old_end_time).\
               update(start_time=new_start_time, end_time=new_end_time)

    def validate_washing_machine_id(self, washing_machine_id: str):
        is_valid_washing_machine_id = WashingMachine.objects.filter(washing_machine_id=washing_machine_id).exists()
        is_invalid_washing_machine_id = not is_valid_washing_machine_id
        if is_invalid_washing_machine_id:
            raise InvalidWashingMachineId
        return

    def validate_day(self, day: Days):
        days = [day.value for day in Days]
        if day not in days:
            raise InvalidDay
        return

    def check_if_start_time_less_than_end_time(self, start_time, end_time):
        if start_time>end_time:
            raise StartTimeGreaterThanEndTimeError
        return
