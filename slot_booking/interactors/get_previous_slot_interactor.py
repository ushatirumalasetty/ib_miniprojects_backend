from slot_booking.interactors.storages.get_previous_slots_interface \
import StorageInterface
from slot_booking.interactors.presenters.presenter_interface import\
PresenterInterface
from typing import List
import datetime
from slot_booking.constants.enums import *
from slot_booking.exceptions.exceptions import *


class GetPreviousSlotsInteractor:
    def __init__(self, storage: StorageInterface,presenter: PresenterInterface):
        self.storage = storage
        self.presenter=presenter
 
    def get_previous_slots_interactor(self, user_id:int):

        previous_slots_dto = self.storage.get_previous_slots(user_id=user_id)
        return self.presenter.\
        get_reponse_for_previous_slots_list(
            previous_slots_list=previous_slots_dto)
