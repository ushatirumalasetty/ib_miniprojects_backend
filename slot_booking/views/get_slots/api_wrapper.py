import json

from django.http import HttpResponse

from slot_booking.interactors.get_avilable_slots_interactor import \
    GetAvilableSlotsInteractor
from slot_booking.presenters.presenter_implementation import PresenterImplementation


from slot_booking.storages.get_avilable_slots_implementation import StorageImplementation


def api_wrapper(*args, **kwargs):
    
    user = kwargs['user']
    
    user_id = user.id
    
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetAvilableSlotsInteractor(storage=storage,presenter=presenter)
    
    slots_dict = interactor.get_slots_for_particular_days_with_avilablity_status(user_id=user_id)
    
    response_data = json.dumps(slots_dict)
    return HttpResponse(response_data, status=200)
