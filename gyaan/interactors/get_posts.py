from typing import List
from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
import datetime



@dataclass
class PostDTO:
    post_id: int
    posted_at: datetime.datetime
    posted_by_id: int
    title: str
    content: str


@dataclass
class CommentDTO:
    comment_id: int
    commented_at: datetime.datetime
    commented_by_id: int
    content: str


@dataclass
class Tag:
    tag_id: int
    name: str


@dataclass
class PostTag:
    post_id: int
    tag_id: int


@dataclass
class PostTagDetails:
    tags: List[Tag]
    post_tag_ids: List[PostTag]


@dataclass
class PostReactionsCount:
    post_id: int
    reactions_count: int


@dataclass
class CommentReactionsCount:
    comment_id: int
    reactions_count: int


@dataclass
class PostCommentsCount:
    post_id: int
    comments_count: int


@dataclass
class CommentRepliesCount:
    comment_id: int
    replies_count: int


@dataclass
class UserDetailsDTO:
    user_id: int
    name: str
    profile_pic_url: str


@dataclass()
class CompletePostDetails:
    post_dtos: List[PostDTO]
    post_reaction_counts: List[PostReactionsCount]
    comment_reaction_counts: List[CommentReactionsCount]
    comment_counts: List[PostCommentsCount]
    reply_counts: List[CommentRepliesCount]
    comment_dtos: List[CommentDTO]
    post_tag_ids: List[PostTag]
    tags: List[Tag]
    users_dtos: List[UserDetailsDTO]


class StorageInterface(ABC):

    @abstractmethod
    def get_post_details(self, post_ids: List[int]) -> List[
        PostDTO]:
        pass
    
    @abstractmethod
    def get_users_details(self,user_ids:List[int]):
        pass


    @abstractmethod
    def get_post_tags(self, post_ids: List[int]) -> PostTagDetails:
        pass

    @abstractmethod
    def get_post_reactions_count(self, post_ids: List[int]) -> \
            List[PostReactionsCount]:
        pass

    @abstractmethod
    def get_post_comments_count(self, post_ids: List[int]) -> \
            List[PostCommentsCount]:
        pass

    @abstractmethod
    def get_comment_reactions_count(self, comment_ids: List[int]) -> \
            List[CommentReactionsCount]:
        pass

    @abstractmethod
    def get_comment_replies_count(self, comment_ids: List[int]) -> \
            List[CommentRepliesCount]:
        pass

    @abstractmethod
    def get_comment_details(self, comment_ids: List[int]) -> List[CommentDTO]:
        pass

    @abstractmethod
    def get_latest_comment_ids(self, post_id, no_of_comments) -> List[int]:
        pass

    @abstractmethod
    def get_valid_post_ids(self, post_ids: List[int]) -> List[int]:
        pass


class InvalidPostIds(Exception):
    def __init__(self, invalid_post_ids):
        self.invalid_post_ids = invalid_post_ids


class PresenterInterface(ABC):
    @abstractmethod
    def raise_exception_for_invalid_post_ids(self, err: InvalidPostIds):
        pass

    @abstractmethod
    def get_posts_response(self, post_details: CompletePostDetails):
        pass





class GetPostsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_posts_wrapper(self, post_ids: List[int],
                          presenter: PresenterInterface):
        try:
            return self._prepare_posts_response(
                post_ids=post_ids,
                presenter=presenter
            )
        except InvalidPostIds as err:
            presenter.raise_exception_for_invalid_post_ids(err)

    def _prepare_posts_response(self, post_ids: List[int],
                                presenter: PresenterInterface):
        completed_post_details = self.get_posts(post_ids=post_ids)
        return presenter.get_posts_response(completed_post_details)

    def get_posts(self, post_ids: List[int]):
        unique_post_ids = self._get_unique_post_ids(post_ids)

        self._validate_post_ids(post_ids=unique_post_ids)

        post_dtos = self.storage.get_post_details(
            post_ids=post_ids
        )

        post_tag_details = self.storage.get_post_tags(post_ids=post_ids)

        post_reaction_counts = self.storage.get_post_reactions_count(
            post_ids=post_ids
        )
        posts_comment_counts = self.storage.get_post_comments_count(
            post_ids=post_ids
        )

        comment_ids = self._get_latest_comment_ids(post_ids=post_ids)

        comment_reaction_counts = \
            self.storage.get_comment_reactions_count(comment_ids=comment_ids)

        comment_replies_counts = \
            self.storage.get_comment_replies_count(comment_ids=comment_ids)

        comment_dtos = self.storage.get_comment_details(
            comment_ids=comment_ids
        )

        user_ids = [post_dto.posted_by_id for post_dto in post_dtos]
        user_ids += [
            comment_dto.commented_by_id for comment_dto in comment_dtos
        ]

        user_dtos = self.storage.get_users_details(user_ids=user_ids)

        return CompletePostDetails(
            post_dtos=post_dtos,
            post_reaction_counts=post_reaction_counts,
            comment_counts=posts_comment_counts,
            comment_reaction_counts=comment_reaction_counts,
            reply_counts=comment_replies_counts,
            comment_dtos=comment_dtos,
            post_tag_ids=post_tag_details.post_tag_ids,
            tags=post_tag_details.tags,
            users_dtos=user_dtos
        )

    def _get_latest_comment_ids(self, post_ids):
        comment_ids = []
        for post_id in post_ids:
            comment_ids += self.storage.get_latest_comment_ids(
                post_id=post_id, no_of_comments=2
            )
        return comment_ids

    @staticmethod
    def _get_unique_post_ids(post_ids):
        return list(set(post_ids))

    def _validate_post_ids(self, post_ids):
        valid_post_ids = self.storage.get_valid_post_ids(post_ids)

        invalid_post_ids = [
            post_id
            for post_id in post_ids if post_id not in valid_post_ids
        ]
        if invalid_post_ids:
            raise InvalidPostIds(invalid_post_ids=invalid_post_ids)
        return 
