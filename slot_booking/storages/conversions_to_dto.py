from slot_booking.interactors.storages.dtos import *


def convert_to_washing_machine_wise_slot_dto(washing_machine_slots_obj):
    return WashingMachineWiseSlotDto(
            start_time=washing_machine_slots_obj.start_time.strftime("%H:%M%p"),
            end_time=washing_machine_slots_obj.end_time.strftime("%H:%M %p"))

def convert_to_dto_list(washing_machine_slots_objs_list):
        slot_timings_dtos_list=[]
        for washing_machine_slots_obj in washing_machine_slots_objs_list:
            slot_timings_dto=convert_to_washing_machine_wise_slot_dto(
                                                      washing_machine_slots_obj)
            slot_timings_dtos_list.append(slot_timings_dto)
        return slot_timings_dtos_list

def convert_to_previous_or_upcomming_slots_dto(user_previous_slot_obj):
    return PreviousOrUpcommingSlotsDto(
            start_time=user_previous_slot_obj.start_time.strftime("%H:%M %p"),
            end_time=user_previous_slot_obj.end_time.strftime("%H:%M %p"),
            washing_machine_slot_id=user_previous_slot_obj.washing_machine_slot_id,
            date=user_previous_slot_obj.date.strftime("%Y-%m-%d"))

def convert_to_previous_or_upcomming_slots_dto_list(user_previous_or_upcomming_slots_obj_list):
        user_previous_or_upcomming_slots_dtos_list=[]
        for  user_previous_or_upcomming_slot_obj in user_previous_or_upcomming_slots_obj_list:
            user_previous_or_upcomming_slots_dto=convert_to_previous_or_upcomming_slots_dto(user_previous_or_upcomming_slot_obj)
            user_previous_or_upcomming_slots_dtos_list.\
            append(user_previous_or_upcomming_slots_dto)
        return user_previous_or_upcomming_slots_dtos_list
    
def convert_to_slots_complete_details_dto(slots_status_dto_list, date_obj):      
    slot_complete_details_dto=SlotCompleteStatusDto(
            date= date_obj,
            slots= slots_status_dto_list
        )
    return slot_complete_details_dto
    

def convert_to_washing_details_dto(washing_machines_obj):
    return WashingMachineDto(
        washing_machine_id=washing_machines_obj.washing_machine_id,
        status=washing_machines_obj.status
        )


def convert_to_washing_details_dto_list(washing_machines_obj_list):
    washing_machines_details_list = []    
    for washing_machines_obj in washing_machines_obj_list:
        washing_machine_dto = convert_to_washing_details_dto(washing_machines_obj)
        washing_machines_details_list.append(washing_machine_dto)
    return washing_machines_details_list


def  convert_to_slots_dto(start_time,end_time,is_avilable):
    return SlotStatusDto(
            start_time=start_time,
            end_time=end_time,
            is_avilable=is_avilable)
