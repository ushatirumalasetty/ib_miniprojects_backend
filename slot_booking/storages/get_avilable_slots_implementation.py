from typing import Optional, List
from slot_booking.interactors.storages.storage_interface import \
    StorageInterface
from slot_booking.models.user import *
import datetime
from datetime import timedelta, date
from slot_booking.interactors.storages.dtos import *
from .conversions_to_dto import *

class StorageImplementation(StorageInterface):

    def get_slots_for_particular_days_with_avilablity_status(self, user_id:int):

        today_date = datetime.now().date()

        list_of_user_booked_dates = list(UserSlot.objects.filter(user_id = user_id)\
                                    .values_list("date", flat=True))


        no_of_days_to_be_displayed = DaysRange.objects.get(id=1).days_range

        list_of_dates_to_be_displayed = []

        washing_machines_obj_list = WashingMachine.objects.all()

        for no in range(no_of_days_to_be_displayed):
            new_date = today_date+timedelta(no+1)
            list_of_dates_to_be_displayed.append(new_date)

        slots_status_dto_list = []
        has_upcomming_date = False
        for user_booked_date in list_of_user_booked_dates:
            if user_booked_date > today_date:
                has_upcomming_date = True
                
        
        slot_complete_details_dto_list=[]
        
        if list_of_user_booked_dates == []:
            for date_obj in list_of_dates_to_be_displayed:
                for washing_machine_obj in washing_machines_obj_list:
                        if washing_machine_obj.status == "ACTIVE":
                            day_of_date = date_obj.strftime("%A").upper()
                            slots_obj_list = WashingMachineSlot.objects.filter(day=day_of_date,washing_machine=washing_machine_obj)
                            for slot_obj in slots_obj_list:
                                start_time = slot_obj.start_time
                                end_time=slot_obj.end_time
                                is_slot_booked = UserSlot.objects.\
                                filter(date=date_obj,washing_machine_id=washing_machine_obj.id,
                                start_time=start_time, end_time = end_time)
                                if is_slot_booked:
                                    slot_status_dto = convert_to_slots_dto(start_time=start_time,end_time=end_time,is_avilable=False)
                                else:
                                    slot_status_dto = convert_to_slots_dto(start_time=start_time,end_time=end_time,is_avilable=True)
                                    slots_status_dto_list.append(slot_status_dto)
                slot_complete_details_dto = convert_to_slots_complete_details_dto(slots_status_dto_list,date_obj)        
                slot_complete_details_dto_list.append(slot_complete_details_dto)
                slots_status_dto_list=[]
             
                           
            return slot_complete_details_dto_list
        else:
            if has_upcomming_date:
                    for date_obj in list_of_dates_to_be_displayed:
                        for washing_machine_obj in washing_machines_obj_list:
                            day_of_date = date_obj.strftime("%A").upper()
                            slots_obj_list = WashingMachineSlot.objects.filter(day=day_of_date,washing_machine=washing_machine_obj)
                            for slot_obj in slots_obj_list:
                                start_time = slot_obj.start_time
                                end_time = slot_obj.end_time
                                slot_status_dto = convert_to_slots_dto(start_time=start_time,end_time=end_time,is_avilable=False)
                                slots_status_dto_list.append(slot_status_dto)
                        slot_complete_details_dto = convert_to_slots_complete_details_dto(slots_status_dto_list,date_obj)        
                        slot_complete_details_dto_list.append(slot_complete_details_dto)
                        slots_status_dto_list=[]
             
                        
            else:
                    for date_obj in list_of_dates_to_be_displayed:
                        for washing_machine_obj in washing_machines_obj_list:
                            if washing_machine_obj.status == "ACTIVE":
                                day_of_date = date_obj.strftime("%A").upper()
                                slots_obj_list = WashingMachineSlot.objects.filter(day=day_of_date,washing_machine=washing_machine_obj)
                                for slot_obj in slots_obj_list:
                                    start_time = slot_obj.start_time
                                    end_time=slot_obj.end_time
                                    is_slot_booked = UserSlot.objects.\
                                    filter(date=date,washing_machine_id=washing_machine_obj.id,
                                    start_time=start_time, end_time = end_time)
                                    if is_slot_booked:
                                        slot_status_dto = convert_to_slots_dto(start_time=start_time,end_time=end_time,is_avilable=False)
                                    else:
                                        slot_status_dto = convert_to_slots_dto(start_time=start_time,end_time=end_time,is_avilable=True)
     
             
                                    slots_status_dto_list.append(slot_status_dto)
                        slot_complete_details_dto = convert_to_slots_complete_details_dto(slots_status_dto_list,date_obj)        
                        slot_complete_details_dto_list.append(slot_complete_details_dto)
                        slots_status_dto_list=[]
             
            
            return slot_complete_details_dto_list
