import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from slot_booking.interactors.update_washing_machine_slots_interactor import \
    UpdateWashingMachineWiseDaySlotsInteractor
from slot_booking.presenters.presenter_implementation import PresenterImplementation
from slot_booking.storages.add_washing_machine_wise_day_slots_implementation import StorageImplementation


def api_wrapper(*args, **kwargs):
    request_data = kwargs['request_data']
    washing_machine_id = request_data['washing_machine_id']
    day = request_data['day']
    old_start_time =request_data['old_start_time']
    old_end_time=request_data['old_end_time']
    new_start_time =request_data['new_start_time']
    new_end_time=request_data['new_end_time']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = UpdateWashingMachineWiseDaySlotsInteractor(storage=storage,presenter=presenter)

    interactor.add_washing_machine_wise_day_wise_slots(
        washing_machine_id=washing_machine_id,
        day=day,
        old_start_time=old_start_time,
        old_end_time=old_end_time,
        new_start_time=new_start_time,
        new_end_time=new_end_time)

  
    return HttpResponse(status=201)
