from typing import Optional, List
from slot_booking.interactors.storages.get_upcomming_slots_interface import *
from slot_booking.models.user import *
from slot_booking.constants.enums import *
from slot_booking.exceptions.exceptions import *
from datetime import date
from slot_booking.interactors.storages.dtos import *
from .conversions_to_dto import convert_to_previous_or_upcomming_slots_dto_list
from django.db.models import Q

class StorageImplementation(StorageInterface):

    def get_upcomming_slots(self,user_id):
        today=date.today()
        time=datetime.now().time()
        user_upcomming_slots_obj_list = UserSlot.objects.filter(user_id = user_id).filter(Q(date__gt=today)|Q(date__gte=today, start_time__gt=time))
        user_upcomming_slots_dto = convert_to_previous_or_upcomming_slots_dto_list(user_upcomming_slots_obj_list)
        return user_upcomming_slots_dto
