from formaster.interactors.base import \
    BaseSubmitFormResponseInteractor
from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass

class StorageInterface(ABC):
    @abstractmethod 
    def get_option_ids_for_question(self, question_id:int):
        pass


class MCQQuestionSubmitFormResponseInteractor(
        BaseSubmitFormResponseInteractor):

    def __init__(self, storage: StorageInterface, question_id: int,
                 form_id: int, user_id: int, user_submitted_option_id: int):
        super().__init__(storage, question_id, form_id, user_id)
        self.user_submitted_option_id = user_submitted_option_id

    def _validate_user_response(self):
# TODO: get option ides for the question
        option_ids = self.storage.get_option_ids_for_question(self.question_id)
# TODO: check if option id if valid
        if self.user_submitted_option_id not in option_ids:
            raise InvalidUserResponseSubmit
# TODO: create user response
    def _create_user_response(self) -> int:
        user_response_dto = UserResponseDTO(
            self.user_id, self.question_id, self.user_submitted_option_id
        )
        response_id = self.storage.create_user_mcq_response(user_response_dto)
        return response_id

class InvalidUserResponseSubmit(Exception):
    pass


@dataclass
class UserResponseDTO:
        user_id:int
        question_id:int
        user_submitted_option_id:int
