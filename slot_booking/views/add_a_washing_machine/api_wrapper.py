import json

from django.http import HttpResponse
from slot_booking.interactors.add_a_washing_machine_interactor import \
    AddAWashingMachineInteractor
from slot_booking.presenters.presenter_implementation import PresenterImplementation
from slot_booking.storages.add_a_washing_machine_implementation import StorageImplementation


def api_wrapper(*args, **kwargs):
    
    request_data = kwargs['request_data']
    washing_machine_id = request_data['washing_machine_id']
    status=request_data['status']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = AddAWashingMachineInteractor(storage=storage,presenter=presenter)
    
    interactor.add_a_washing_machine_interactor(washing_machine_id=washing_machine_id, status=status)
    
    return HttpResponse(status=201)
