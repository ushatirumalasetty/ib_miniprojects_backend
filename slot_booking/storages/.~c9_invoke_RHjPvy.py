from typing import Optional, List
from slot_booking.interactors.storages.get_previous_slots_interface import *
from slot_booking.models.user import *
from slot_booking.constants.enums import *
from slot_booking.exceptions.exceptions import *
from datetime import date
from slot_booking.interactors.storages.dtos import *
from .conversions_to_dto import convert_to_previous_or_upcomming_slots_dto_list
from django.db.models import Q

class StorageImplementation(StorageInterface):

    def get_previous_slots(self,user_id,offset,limit):
        today=date.today()
        time=datetime.today().time()
        user_previous_slots_obj_list = UserSlot.objects.filter(user__id = user_id)\
        .filter(Q(date__lt=today))[offset:offset+limit]
        user_previous_slots_dto =convert_to_previous_or_upcomming_slots_dto_list(user_previous_slots_obj_list)
        return user_previous_slots_dto
