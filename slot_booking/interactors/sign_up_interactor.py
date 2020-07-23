from slot_booking.interactors.storages.storage_interface import StorageInterface
from slot_booking.interactors.presenters.presenter_interface import PresenterInterface
from .common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from .common.oauth2_storage import OAuth2SQLStorage

class UserSignInteractor:
    def __init__(self, storage: StorageInterface ,oauth2_storage: OAuth2SQLStorage, presenter: PresenterInterface):
        self.storage = storage
        self.presenter=presenter
        self.oauth2_storage = oauth2_storage
        
    def user_signup(self, username:str, password: str, confirm_password:str):
        try:
            self.storage.validate_user_name(username=username)
        except:
            self.presenter.raise_exception_for_invalid_username()
            return 

        try:
            user_id = self.storage.validate_password(username=username, password=password)
        except:
            self.presenter.raise_exception_for_invalid_password()
            return 

        try:
            user_id = self.storage.\
            check_if_confirm_password_match_password(username=username, 
                                                     password=password,
                                                     confirm_password=confirm_password)
        except:
            self.presenter.raise_exception_for_password_didnt_match()
            return 
        
        
        interactor = OAuthUserAuthTokensService(oauth2_storage=self.oauth2_storage)
        dto = interactor.create_user_auth_tokens(self, user_id)
        response = self.presenter.get_token_response_dto(dto=dto)
        return response
    