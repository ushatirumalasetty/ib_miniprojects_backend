from unittest.mock import create_autospec
from gyaan.interactors.get_posts import *
import pytest
from .conftest import *

class TestGetPosts:
    def test_given_invalid_post_ids(self):
        post_ids=[1,3,4,-1]
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetPostsInteractor(storage)
        storage.get_valid_post_ids.return_value = [1,3,4]
        invalid_post_ids=[-1]

        interactor.submit_form_response_wrapper(post_ids=post_ids,presenter=presenter)

        call_obj = presenter.raise_exception_for_invalid_post_ids.call_args
        
        error_object = call_obj.args[0]
        
        assert error_object.invalid_post_ids==invalid_post_ids
    
    def test_get_valid_details(self):

        post_ids=[1]
        
        expected_dto = complete_post_details_dto  
        
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetPostsInteractor(storage)
        
        actual_dto = interactor.get_posts_wrapper(post_ids=post_ids,
                          presenter=presenter)
        assert expected_dto == actual_dto
        
        



class NotFound(Exception):
    pass
