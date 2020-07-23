from typing import List
from slot_booking.interactors.storages.get_washig_machines_details_interface\
import StorageInterface
from slot_booking.models.user import WashingMachine
from slot_booking.constants.enums import *
from slot_booking.exceptions.exceptions import *
from .conversions_to_dto import *

class StorageImplementation(StorageInterface):


    def get_washing_machines_details(self):

        washing_machines_obj_list = WashingMachine.objects.all()

        washing_machine_details_dto_list = convert_to_washing_details_dto_list(
            washing_machines_obj_list )

        return washing_machine_details_dto_list
