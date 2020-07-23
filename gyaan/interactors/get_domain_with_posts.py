from gyaan.interactors.get_domine_interactor import *
from gyaan.interactors.get_posts import *
from gyaan.interactors.get_domain_posts import *
from dataclasses import dataclass

class DomainWithPosts:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_domain_with_posts_wrapper(self, user_id: int, domain_id: int,
                                      offset: int, limit: int,
                                      presenter: PresenterInterface):

        try:
            return self._get_domain_with_posts_response(
                user_id=user_id, domain_id=domain_id,
                offset=offset, limit=limit,
                presenter=presenter
            )
#TODO: validate domine id
        except DomainDoesNotExist:
            presenter.raise_domain_does_not_exist_exception()
#TODO: validate is user is a domine member
        except UserNotDomainMember:
            presenter.raise_user_not_domain_member_exception()

    def _get_domain_with_posts_response(self, user_id: int, domain_id: int,
                                        offset: int, limit: int,
                                        presenter: PresenterInterface):

        domain_with_posts_dto = self.get_domain_with_posts(
            user_id=user_id,
            domain_id=domain_id,
            offset=offset,
            limit=limit
        )

        return presenter.get_domain_with_posts_response(domain_with_posts_dto)

    def get_domain_with_posts(self, user_id: int, domain_id: int,
                              offset: int, limit: int):
#TODO: get domine details
        domain_details_interactor = GetDomineInteractor(
            storage=self.storage
        )

        domain_details = domain_details_interactor.get_domain_details(
            user_id=user_id,
            domine_id=domain_id
        )
#TODO: get domine posts
        domain_posts_interactor = DomainPostsInteractor(
            storage=self.storage
        )
        domain_posts = domain_posts_interactor.get_domain_posts(
            user_id=user_id,
            domain_id=domain_id,
            offset=offset,
            limit=limit
        )

        return DomainDetailsWithPosts(
            domain_details=domain_details,
            post_details=domain_posts
        )

class DomainDoesNotExist(Exception):
    pass


@dataclass
class DomainDetailsWithPosts:
    post_details: CompletePostDetails
    domain_details: DomainDetailsDTO
