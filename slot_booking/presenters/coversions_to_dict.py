from slot_booking.interactors.storages.dtos import *
from slot_booking.constants.constants import *

def convert_dto_to_dict(ListWashingMachineWiseSlotDto):
        washing_machine_wise_day_slots_list= []
        for WashingMachineWiseSlotDto in ListWashingMachineWiseSlotDto:
            washing_machine_wise_day_slots_dict = {
                "start_time": WashingMachineWiseSlotDto.start_time,
                "end_time": WashingMachineWiseSlotDto.end_time,
            }
            washing_machine_wise_day_slots_list.append(washing_machine_wise_day_slots_dict)
        return washing_machine_wise_day_slots_list

def convert_previous_slot_dto_to_dict(PreviousorUpcommingSlotsDtoList):
        user_previous_or_upcomming_slots_list= []
        for PreviousorUpcommingSlotsDto in PreviousorUpcommingSlotsDtoList:
            user_previous_or_upcomming_slots_dict = {
                "start_time": PreviousorUpcommingSlotsDto.start_time,
                "end_time": PreviousorUpcommingSlotsDto.end_time,
                "washing_machine_id":PreviousorUpcommingSlotsDto.washing_machine_id,
                "date":PreviousorUpcommingSlotsDto.date
            }
            user_previous_or_upcomming_slots_list.append(user_previous_or_upcomming_slots_dict)
        return user_previous_or_upcomming_slots_list

def convert_washing_machines_details_dtos_list_to_dict(washing_machines_details_dtos_list):
    washing_machines_details_list=[]
    for washing_machines_details_dto in washing_machines_details_dtos_list:
        washing_machines_details_dict={
            "washing_machine_id": washing_machines_details_dto.washing_machine_id,
            "status": washing_machines_details_dto.status
        }
        washing_machines_details_list.append(washing_machines_details_dict)
    return washing_machines_details_list
    

    
def convert_datewise_slots_till_range_dtos_list_to_dict(avilable_slots):
    datewise_slots_till_range_dtos_list=[]
    slot_complete_details_list=[]
    for datewise_slots_till_range_dto in avilable_slots:
        date=datewise_slots_till_range_dto.date.strftime("%Y-%m-%d")
        for slot in datewise_slots_till_range_dto.slots:
            datewise_slots_till_range_dict={
                "start_time": slot.start_time.strftime("%H:%M %p"),
                "end_time": slot.end_time.strftime("%H:%M %p"),
                "is_available": slot.is_avilable
            }
            datewise_slots_till_range_dtos_list.append(datewise_slots_till_range_dict)
        slots_complete_details={
            "date": date,
            "slots":datewise_slots_till_range_dtos_list
            }
        datewise_slots_till_range_dtos_list=[]
        slot_complete_details_list.append(slots_complete_details)    
    return slot_complete_details_list
        
    
def convert_responses_of_an_dto_to_dict(requests_details_dto):
    requests_details_list=[]
    for user in requests_details_dto.users:
            user_id=user.user_id
            user_name=user.user_name
            first_name=user.first_name
            last_name=user.last_name
            for requests_dto in requests_details_dto.requests:
                if user_id == requests_dto.user_id:
                    date= requests_dto.date
                    washing_machine_id = requests_dto.washing_machine_id
                    slot_start_time= requests_dto.slot_start_time
                    slot_end_time= requests_dto.slot_end_time
                    request_status= requests_dto.request_status
            
                    requests_details_dict={
                        "user": {
                            "user_id": user_id,
                            "user_name": user_name,
                            "first_name": first_name,
                            "last_name": last_name
                        },
                        "date": date,
                        "washing_machine_id": washing_machine_id,
                        "slot_start_time": slot_start_time,
                        "slot_end_time": slot_end_time,
                        "request_status": request_status
                    }
            requests_details_list.append(requests_details_dict)
    return requests_details_list