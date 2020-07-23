import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from slot_booking.interactors.get_washing_machines_details_interactor import \
    GetWashingMachinesDetailsInteractor
from slot_booking.presenters.presenter_implementation import PresenterImplementation
from slot_booking.storages.get_washing_machines_details_implementation import StorageImplementation


def api_wrapper(*args, **kwargs):
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetWashingMachinesDetailsInteractor(storage=storage, presenter=presenter)

    washing_machine_details_list = interactor.get_washing_machines_details_interactor()

    response_data = json.dumps(washing_machine_details_list)
    return HttpResponse(response_data, status=200)
