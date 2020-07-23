from typing import Optional, List
from slot_booking.interactors.storages.get_washing_machine_wise_storage_interface import \
    StorageInterface
from slot_booking.models.user import WashingMachineSlot
from slot_booking.constants.enums import *
from slot_booking.exceptions.exceptions import *
from .conversions_to_dto import *
from slot_booking.constants.enums import *
from slot_booking.models.user import *

class StorageImplementation(StorageInterface):


    def get_washing_machine_wise_day_wise_slots(self,day:Days,
                                                     washing_machine_id:str):

        self.validate_washing_machine_id(washing_machine_id=washing_machine_id)

        self.validate_if_day_belong_to_washing_machine(day=day,
                                        washing_machine_id=washing_machine_id)

        washing_machine_related_slots_on_a_day_obj_list = WashingMachineSlot.\
        objects.filter(day=day,
                       washing_machine__washing_machine_id=washing_machine_id)

        washing_machine_related_slots_on_a_day_dto_list = convert_to_dto_list(
            washing_machine_related_slots_on_a_day_obj_list)

        return washing_machine_related_slots_on_a_day_dto_list
    
    
    def validate_washing_machine_id(self, washing_machine_id: str):
        
        is_valid_washing_machine_id = WashingMachine.objects.\
        filter(washing_machine_id=washing_machine_id).exists()
        
        is_invalid_washing_machine_id = not is_valid_washing_machine_id
        
        if is_invalid_washing_machine_id:
            raise InvalidWashingMachineId
   

    def validate_if_day_belong_to_washing_machine(self, day:Days,
                                                  washing_machine_id:str):
        
        washing_machines=WashingMachine.objects.\
        filter(washing_machine_id=washing_machine_id)
        
        is_day_belong_to_washing_machine=WashingMachineSlot.objects.\
        filter(washing_machine=washing_machines[0],day=day).exists()
        
        is_day_doesnt_belong_to_washing_machine = not is_day_belong_to_washing_machine
        
        if is_day_doesnt_belong_to_washing_machine:
            raise DayDoesntBelongToWashingMachine
