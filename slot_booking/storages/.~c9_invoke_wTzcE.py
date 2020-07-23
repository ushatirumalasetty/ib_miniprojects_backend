from typing import Optional, List
from slot_booking.interactors.storages.book_a_slot_interface import \
    StorageInterface
from slot_booking.models.user import *
import datetime
from datetime import timedelta, date
from slot_booking.interactors.storages.dtos import *
from .conversions_to_dto import *

class StorageImplementation(StorageInterface):

    def book_a_slot(self, date,start_time, end_time, user_id:int):
        format = "%d-%b-%Y"
        datetime_str = datetime.strptime(date_time, format) 
        washing_machines_obj_list = WashingMachine.objects.all()

        for washing_machine_obj in washing_machines_obj_list:
                        if washing_machine_obj.status == "ACTIVE":
                            day_of_date = datetime_str.strftime("%A").upper()
                            slots_obj_list = WashingMachineSlot.objects.filter(day=day_of_date,washing_machine=washing_machine_obj)
                            for slot_obj in slots_obj_list:
                                start_time = slot_obj.start_time
                                end_time=slot_obj.end_time
                                is_slot_booked = UserSlot.objects.\
                                filter(date=date,washing_machine_id=slot_obj.id,
                                start_time=start_time, end_time = end_time)
                                if not is_slot_booked:
                                    UserSlot.objects.\
                                    create(user_id=user_id,date=date,washing_machine_id=slot_obj.id,
                                    start_time=start_time, end_time = end_time)
                                    return 
