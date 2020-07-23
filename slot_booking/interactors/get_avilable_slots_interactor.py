from slot_booking.interactors.storages.storage_interface \
import StorageInterface
from slot_booking.interactors.presenters.presenter_interface import\
PresenterInterface
from typing import List
import datetime
from slot_booking.constants.enums import *

class GetAvilableSlotsInteractor:
    def __init__(self, storage: StorageInterface,presenter: PresenterInterface):
        self.storage = storage
        self.presenter=presenter

    def get_slots_for_particular_days_with_avilablity_status(self, user_id:int):
        list_of_datewise_slots = self.storage.\
                                 get_slots_for_particular_days_with_avilablity_status(user_id = user_id)
        return self.presenter.\
               get_response_of_list_of_datewise_slots_till_range(list_of_datewise_slots)

