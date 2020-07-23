from slot_booking.interactors.storages.get_washig_machines_details_interface \
import StorageInterface
from slot_booking.interactors.presenters.presenter_interface import\
PresenterInterface
from typing import List
import datetime
from slot_booking.constants.enums import *
from slot_booking.exceptions.exceptions import *


class GetWashingMachinesDetailsInteractor:
    def __init__(self, storage: StorageInterface,presenter: PresenterInterface):
        self.storage = storage
        self.presenter=presenter
 
    def get_washing_machines_details_interactor(self):
        washing_machines_details_dto = self.storage.get_washing_machines_details()
        return self.presenter.\
        get_response_for_washing_machines_details(
            washing_machines_details_dtos_list=washing_machines_details_dto)
        