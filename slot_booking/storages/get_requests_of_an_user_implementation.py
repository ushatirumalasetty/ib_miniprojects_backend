from typing import Optional, List
from slot_booking.interactors.storages.get_requests_of_an_user_interface import *
from slot_booking.models.user import *
from slot_booking.constants.enums import *
from slot_booking.exceptions.exceptions import *
from datetime import date,time
from slot_booking.interactors.storages.dtos import *
from django.db.models import Q

class StorageImplementation(StorageInterface):

    def get_requests_details_of_an_user(self,user_id):
        requested_user_details_dto_list=[]
        requested_request_details_dto_list=[]
        request_objs=Request.objects.all()
        for request_obj in request_objs:
            requested_user_details_dto=self._convert_to_user_details_dto(request_obj)
            requested_request_details_dto=self._convert_to_request_details_dto(request_obj)
            requested_user_details_dto_list.append(requested_user_details_dto)
            requested_request_details_dto_list.append(requested_request_details_dto)
        request_complete_details_dto_list = self._convert_to_request_complete_details_dto(requested_user_details_dto_list, requested_request_details_dto_list)
    
        return request_complete_details_dto_list
        
    def _convert_to_user_details_dto(self, request_obj):
        user_dto = UserDetailsDto(
            user_id=request_obj.requested_by.id,
            first_name=request_obj.requested_by.first_name,
            last_name=request_obj.requested_by.last_name,
            user_name=request_obj.requested_by.user_name
            )
        return user_dto
            
    def _convert_to_request_details_dto(self, request_obj):
        return RequestDetailsDto(
            user_id=request_obj.requested_by.id,
            date=request_obj.date,
            washing_machine_id=request_obj.requested_user_slot.\
            washing_machine.washing_machine_id,
            slot_start_time=request_obj.requested_user_slot.start_time,
            slot_end_time=request_obj.requested_user_slot.end_time,
            request_status=request_obj.request_status
            )
            
    def _convert_to_request_complete_details_dto(self, 
                                                list_of_user_dtos, list_of_requests_dtos):
        return RequestCompleteDetailsDto(
            users=list_of_user_dtos,
            requests=list_of_requests_dtos
            )