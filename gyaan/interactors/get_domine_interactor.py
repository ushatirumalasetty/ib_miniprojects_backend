from abc import ABC
from abc import abstractmethod
from typing import List
from dataclasses import dataclass

class StorageInterface(ABC):
    @abstractmethod
    def is_user_domain_expert(self, domine_id:int, user_id:int):
        pass

    @abstractmethod
    def get_domain(self, domain_id:int):
        pass

    @abstractmethod
    def is_user_following_domain(self, domine_id:int, user_id:int):
        pass

    @abstractmethod
    def get_domine_stats(self, domine_id:int):
        pass

    @abstractmethod
    def get_domine_expert_ids(self, domine_id:int):
        pass

    @abstractmethod
    def get_users_details(self,domine_experts_ids:List[int]):
        pass

    @abstractmethod
    def get_domine_join_requests(self, domine_id:int):
        pass

    @abstractmethod
    def get_reqested_user_dtos(self,user_ids:List[int]):
        pass


class PresenterInterface(ABC):
    @abstractmethod
    def raise_domain_does_not_exist_exception(self):
        pass

    @abstractmethod
    def raise_user_not_domain_member_exception(self):
        pass
    
    @abstractmethod
    def get_domain_details_response(self,domain_details_dto):
        pass


class GetDomineInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_domain_details_wrapper(self,
                                   domine_id:int,
                                   user_id:int,
                                   presenter=PresenterInterface):
        try:
            self._get_domain_details_response(domain_id=domine_id, user_id=user_id,
                                     presenter=presenter)
        except InvalidDomineId:
            presenter.raise_domain_does_not_exist_exception()
        except UserNotDomainMember:
            presenter.raise_user_not_domain_member_exception()


    def _get_domain_details_response(self, domain_id: int, user_id: int,
                                     presenter: PresenterInterface):
        domain_details_dto = self.get_domain_details(domine_id=domain_id, user_id=user_id)
        response = presenter.get_domain_details_response(
            domain_details_dto)
        return response


    def get_domain_details(self, user_id:int, domine_id:int):
#TODO: get_domine_id
        domain_dto = self.storage.get_domain(domain_id=domine_id)
#TODO: is user following domine

        is_user_following_domain = self.\
        storage.is_user_following_domain(domine_id=domine_id, user_id=user_id)
        if is_user_following_domain:
            raise UserNotDomainMember
#TODO: domine_stats
        domine_stats = self.storage.get_domine_stats(domine_id=domine_id)
#TODO: domine_experts_ids
        domine_experts_ids = self.\
        storage.get_domine_expert_ids(domine_id=domine_id)
#TODO: domine_experts
        domine_experts = self.storage.get_users_details(domine_experts_ids)
#TODO: is user domine expert
#TODO: domine join requests
#TODO: requested user dtos
        is_user_domain_expert, domain_join_requests, requested_user_dtos =self.\
        _get_domine_expert_details(domine_id=domine_id, user_id=user_id)


        response = DomainDetailsDTO(
            domain=domain_dto,
            domain_stats=domine_stats,
            domain_experts=domine_experts,
            user_id=user_id,
            is_user_domain_expert=is_user_domain_expert,
            join_requests=domain_join_requests,
            requested_users=requested_user_dtos
        )
        return response



    def _get_domine_expert_details(self, domine_id:int, user_id:int):
#TODO: is user domine expert
        is_user_domain_expert = self.\
        storage.is_user_domain_expert(user_id=user_id, domine_id=domine_id)
#TODO: domine join requests
        domine_join_requests = []
        requested_user_dtos = []
        if is_user_domain_expert:
            domine_join_requests = self.\
            storage.get_domine_join_requests(domine_id)

#TODO: requested user dtos
        if domine_join_requests:
            requested_user_dtos = self.storage.\
            get_reqested_user_dtos(user_ids=[dto.user_id for dto in domine_join_requests])

        return is_user_domain_expert, domine_join_requests, requested_user_dtos




class InvalidDomineId(Exception):
    pass

class UserNotDomainMember(Exception):
    pass



@dataclass
class DomainDTO:
    domain_id: int
    name: str
    description: str

@dataclass
class DomainStatsDTO:
    domain_id: int
    followers_count: int
    posts_count: int
    bookmarked_count: int

@dataclass
class UserDetailsDTO:
    user_id: int
    name: str
    profile_pic_url: str

@dataclass
class DomainJoinRequestDTO:
    request_id: int
    user_id: int


@dataclass
class DomainDetailsDTO:
    domain=DomainDTO,
    domain_stats=DomainStatsDTO,
    domain_experts=List[UserDetailsDTO],
    user_id:int
    is_user_domain_expert:bool
    join_requests=DomainJoinRequestDTO,
    requested_users=List[UserDetailsDTO]


