import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from slot_booking.interactors.book_a_slot_interactor import \
    BookASlotInteractor
from slot_booking.presenters.presenter_implementation import PresenterImplementation
from slot_booking.storages.book_a_slot_implementation import StorageImplementation


def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    user_id = user.id
    request_data = kwargs['request_data']
    date = request_data['date']
    start_time =request_data['start_time']
    end_time=request_data['end_time']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
  
    interactor = BookASlotInteractor(storage=storage,presenter=presenter)

    interactor.book_a_slot_interactor(
        user_id=user_id,
        date=date,
        start_time=start_time,
        end_time=end_time)
  
    return HttpResponse(status=201)
