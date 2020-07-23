import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from slot_booking.interactors.add_washing_machine_wise_day_slots_interactor import \
    AddWashingMachineWiseDaySlotsInteractor
from slot_booking.presenters.presenter_implementation import PresenterImplementation
from slot_booking.storages.add_washing_machine_wise_day_slots_implementation import StorageImplementation


def api_wrapper(*args, **kwargs):
    print("1111111111")
    request_data = kwargs['request_data']
    washing_machine_id = request_data['washing_machine_id']
    day = request_data['day']
    start_time =request_data['start_time']
    end_time=request_data['end_time']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    print("222222222")
    interactor = AddWashingMachineWiseDaySlotsInteractor(storage=storage,presenter=presenter)

    interactor.add_washing_machine_wise_day_wise_slots(
        washing_machine_id=washing_machine_id,
        day=day,
        start_time=start_time,
        end_time=end_time)
    print("3333333")

    return HttpResponse(status=201)
