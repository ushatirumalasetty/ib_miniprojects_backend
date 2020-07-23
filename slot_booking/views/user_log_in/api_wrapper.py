import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from slot_booking.interactors.login_interactor import \
    UserLginInteractor
from slot_booking.presenters.presenter_implementation import PresenterImplementation
from slot_booking.storages.login_implementation import StorageImplementation
from slot_booking.common.oauth2_storage import OAuth2SQLStorage


def api_wrapper(*args, **kwargs):
    user=kwargs['user']
    request_data = kwargs['request_data']
    username = request_data['username']
    password = request_data['password']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    oauth_storage = OAuth2SQLStorage()
    interactor = UserLginInteractor(storage=storage,presenter=presenter, oauth2_storage=oauth_storage)
    access_token = interactor.login(username=username, password=password)
    response_data = json.dumps(access_token)
    return HttpResponse(response_data, status=200)
