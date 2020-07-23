from slot_booking.interactors.storages.get_requests_of_an_user_interface \
import StorageInterface
from slot_booking.interactors.presenters.presenter_interface import\
PresenterInterface
from typing import List
import datetime
from slot_booking.constants.enums import *
from slot_booking.exceptions.exceptions import *


class GetRequestDetailsInteractor:
    def __init__(self, storage: StorageInterface,presenter: PresenterInterface):
        self.storage = storage
        self.presenter=presenter
 
    def get_request_details_interactor(self, user_id:int):

        request_details_dto = self.storage.get_requests_details_of_an_user(user_id=user_id)
        return self.presenter.\
        get_response_for_get_requests_details_of_an_user(
            requests_details_list=request_details_dto)
        