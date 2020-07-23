from typing import Optional, List
from slot_booking.interactors.storages.add_a_washing_machine_interface import *
from slot_booking.models.user import *
from slot_booking.constants.enums import *
from slot_booking.exceptions.exceptions import *
import datetime
from slot_booking.interactors.storages.dtos import *



class StorageImplementation(StorageInterface):


    def add_a_washing_machine(self,washing_machine_id:str,
                              status:WashingMachineStatus):
        WashingMachine.objects.create(washing_machine_id=washing_machine_id,
        status=status)
    