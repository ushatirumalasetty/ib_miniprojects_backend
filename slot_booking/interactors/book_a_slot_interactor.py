from slot_booking.interactors.storages.book_a_slot_interface \
import StorageInterface
from slot_booking.interactors.presenters.presenter_interface import\
PresenterInterface
from typing import List
import datetime
from slot_booking.models.user import *

class BookASlotInteractor:
    def __init__(self, storage: StorageInterface,presenter: PresenterInterface):
        self.storage = storage
        self.presenter=presenter

    def book_a_slot_interactor(self, date, start_time, end_time, user_id:int):
        
        self.storage.book_a_slot(user_id=user_id,
                                 start_time=start_time,
                                 end_time=end_time,
                                 date=date)
    
