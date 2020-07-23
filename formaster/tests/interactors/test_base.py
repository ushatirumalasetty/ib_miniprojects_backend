import pytest
from formaster.interactors.base import *
from unittest.mock import create_autospec


class TestBaseclass:

    def test_validate_live_form(self):
        question_id=1
        form_id=1
        user_id=1
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = BaseSubmitFormResponseInteractor(storage,question_id,form_id,user_id)
        storage.validate_question_id_with_form.side_effect = QuestionDoesNotBelongToForm
        presenter.raise_question_does_not_belong_to_form_exception.side_effect = NotFound

        with pytest.raises(NotFound):
            interactor.submit_form_response_wrapper(presenter=presenter)
        
        storage.validate_question_id_with_form.\
        assert_called_once_with(question_id=question_id,form_id=form_id)
        presenter.raise_question_does_not_belong_to_form_exception.assert_called_once()

    def test_validate_user_response(self):
        question_id=1
        form_id=1
        user_id=1
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = BaseSubmitFormResponseInteractor(storage,question_id,form_id,user_id)
        storage.get_form.side_effect = True
        presenter.raise_form_closed_exception.side_effect=NotFound
        with pytest.raises(NotFound):
            interactor.submit_form_response_wrapper(presenter=presenter)
        
        storage.get_form.\
        assert_called_once_with(form_id=form_id)
        presenter.raise_form_closed_exception.assert_called_once()

        
'''
    def test_validate_for_live_form(self):
        question_id=1
        form_id=1
        user_id=1
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = BaseSubmitFormResponseInteractor(storage,question_id,form_id,user_id)
        validate_for_live_form.side_effect = FormClosed

        interactor.get_posts_wrapper(post_ids=post_ids,presenter=presenter)

        call_obj = presenter.raise_exception_for_invalid_post_ids.call_args
        
        error_object = call_obj.args[0]
        
        assert error_object.invalid_post_ids==invalid_post_ids
''' 
    
class NotFound(Exception):
    pass