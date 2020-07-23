from slot_booking.exceptions.exceptions import *
from slot_booking.models.user import *

def validate_user_id(user_id:int):
    is_user_id_valid = User.objects.filter(id=user_id)
    is_user_id_invalid = not is_user_id_valid
    if is_user_id_invalid:
        raise InvalidUserId
    return

def validate_washing_machine_id(washing_machine_id: str):
    is_valid_washing_machine_id = WashingMachine.objects.filter(washing_machine_id=washing_machine_id).exists()
    is_invalid_washing_machine_id = not is_valid_washing_machine_id
    if is_invalid_washing_machine_id:
        raise InvalidWashingMachineId
    return
    
def validate_day(day: Days):
    days = [day.value for day in Days]:
    if day not in days:
        raise InvalidDay
    return

def check_if_start_time_less_than_end_time(start_time, end_time):
    if start_time>end_time:
        raise StartTimeGreaterThanEndTimeError
    return

def validate_if_day_belong_to_washing_machine(day:Days,
                                                  washing_machine_id:str):
        washing_machines=WashingMachine.objects.filter(washing_machine_id=washing_machine_id)
        is_day_belong_to_washing_machine=WashingMachineSlot.objects.filter(washing_machine=washing_machines[0],day=day).exists()
        is_day_doesnt_belong_to_washing_machine = not is_day_belong_to_washing_machine
        if is_day_doesnt_belong_to_washing_machine:
            raise DayDoesntBelongToWashingMachine
        return
