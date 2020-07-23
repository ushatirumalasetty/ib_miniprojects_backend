from unittest.mock import create_autospec
from gyaan.interactors.get_domine_interactor import *
import pytest


class TestPreferences:
    def test_given_invalid_domine_id(self):
        domine_id = 22
        user_id=1                
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetDomineInteractor(storage)
        storage.get_domain.side_effect = InvalidDomineId
        presenter.raise_domain_does_not_exist_exception.side_effect = NotFound

        with pytest.raises(NotFound):
            interactor.get_domain_details_wrapper(
                                   domine_id=domine_id,
                                   user_id=user_id,
                                   presenter=presenter)
        
        storage.get_domain.\
        assert_called_once_with(domain_id=domine_id)
        presenter.raise_domain_does_not_exist_exception.assert_called_once()


    def test_given_is_user_following_domine(self):
        domine_id = 22
        user_id=1                
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetDomineInteractor(storage)
        storage.is_user_following_domain.return_value = True
        presenter.raise_user_not_domain_member_exception.side_effect = NotFound

        with pytest.raises(NotFound):
            interactor.get_domain_details_wrapper(
                                   domine_id=domine_id,
                                   user_id=user_id,
                                   presenter=presenter)
        
        storage.is_user_following_domain.\
        assert_called_once_with(domine_id=domine_id, user_id=user_id)
        presenter.raise_user_not_domain_member_exception.assert_called_once()

        
        
    def test_given_valid_details(self):

        domine_id = 22
        user_id=1                
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetDomineInteractor(storage)
        storage.is_user_following_domain.return_value = True
        presenter.raise_user_not_domain_member_exception.side_effect = NotFound

        with pytest.raises(NotFound):
            interactor.get_domain_details_wrapper(
                                   domine_id=domine_id,
                                   user_id=user_id,
                                   presenter=presenter)

        storage.is_user_following_domain.\
        assert_called_once_with(domine_id=domine_id, user_id=user_id)
        presenter.raise_user_not_domain_member_exception.assert_called_once()


class NotFound(Exception):
    pass