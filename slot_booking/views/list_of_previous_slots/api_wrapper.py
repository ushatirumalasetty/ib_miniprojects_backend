import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from slot_booking.interactors.get_previous_slot_interactor import \
    GetPreviousSlotsInteractor
from slot_booking.presenters.presenter_implementation import PresenterImplementation
from slot_booking.storages.get_previous_slots_implementation import StorageImplementation


def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    user_id = user.id
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetPreviousSlotsInteractor(storage=storage,presenter=presenter)

    previous_slots_dict = interactor.get_previous_slots_interactor(user_id=user_id)
    response_data = json.dumps(previous_slots_dict)
    return HttpResponse(response_data, status=200)
