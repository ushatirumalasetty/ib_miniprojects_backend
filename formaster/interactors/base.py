from abc import ABC
from abc import abstractmethod
from formaster.interactors.mixins.form_validation import FormValidationMixin



class StorageInterface(ABC):
    @abstractmethod
    def validate_question_id_with_form(self, question_id:int, form_id:int):
        pass
    
    @abstractmethod
    def get_form(self, form_id:int):
        pass

class PresenterInterface(ABC):
    @abstractmethod
    def submit_form_response_return(self,user_response_id:int):
        pass

    @abstractmethod
    def raise_form_does_not_exist_exception(self):
        pass
    
    @abstractmethod
    def raise_form_closed_exception(self):
        pass
    
    @abstractmethod
    def raise_question_does_not_belong_to_form_exception(self):
        pass
    
    @abstractmethod
    def raise_invalid_user_response_submitted(self):
        pass
    

class BaseSubmitFormResponseInteractor(FormValidationMixin):

    def __init__(self, storage: StorageInterface, question_id: int,
                 form_id: int, user_id: int):
        self.storage = storage
        self.question_id = question_id
        self.form_id = form_id
        self.user_id = user_id

    def submit_form_response_wrapper(self, presenter: PresenterInterface):
        try:
            user_response_id = self.submit_form_response()
            return presenter.submit_form_response_return(user_response_id)
# TODO:validate form
        except FormDoesNotExist:
            presenter.raise_form_does_not_exist_exception()
# TODO:Is form Live
        except FormClosed:
            presenter.raise_form_closed_exception()
# TODO:validate question belongs to form
        except QuestionDoesNotBelongToForm:
            presenter.raise_question_does_not_belong_to_form_exception()
# TODO:validate user Response
        except InvalidUserResponseSubmit:
            presenter.raise_invalid_user_response_submitted()

    def submit_form_response(self):
# TODO:validate form in mixer since mixer is calling
# TODO:Is form Live
        self.validate_for_live_form(self.form_id)
# TODO:validate question belongs to form
        self.storage.validate_question_id_with_form(
            self.question_id, self.form_id)
# TODO:validate user Response
        self._validate_user_response()
# TODO:create user response
        user_response_id = self._create_user_response()

        return user_response_id

    @abstractmethod
    def _validate_user_response(self):
        pass

    @abstractmethod
    def _create_user_response(self) -> int:
        pass


class FormDoesNotExist(Exception):
    pass

class FormClosed(Exception):
    pass

class QuestionDoesNotBelongToForm(Exception):
    pass

class InvalidUserResponseSubmit(Exception):
    pass
