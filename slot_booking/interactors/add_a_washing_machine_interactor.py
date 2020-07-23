from slot_booking.interactors.storages.add_a_washing_machine_interface \
import StorageInterface
from slot_booking.interactors.presenters.presenter_interface import\
PresenterInterface
from typing import List
import datetime
from slot_booking.constants.enums import WashingMachineStatus
from slot_booking.exceptions.exceptions import *
from slot_booking.models.user import *

class AddAWashingMachineInteractor:
    def __init__(self, storage: StorageInterface,presenter: PresenterInterface):
        self.storage = storage
        self.presenter=presenter

    def add_a_washing_machine_interactor(self,
                              washing_machine_id:str,
                              status:WashingMachineStatus):
        
        self.storage.\
        add_a_washing_machine(washing_machine_id=washing_machine_id,status=status)
    

    