import pytest

import datetime

from gyaan.interactors.get_posts import *

@pytest.fixture()
def user_dtos():
    user_dtos = [
        UserDetailsDTO(user_id=1,
            name="usha",
            profile_pic_url="www.google.com")
        ]
    return user_dtos


@pytest.fixture()
def post_dtos():
    post_dtos = [
        PostDTO(post_id=1,
            posted_at=datetime.datetime.now(),
            posted_by_id=1,
            title="whatsapp",
            content="the best app ever")
            ]
    return post_dtos
        

@pytest.fixture()
def comment_dtos():
    comment_dtos = [
       CommentDTO(comment_id=1,
            commented_at=datetime.datetime.now(),
            commented_by_id=1,
            content="yes!ofcourse")
        ]
    return comment_dtos


@pytest.fixture()
def tag_dtos():
    tag_dtos = [
        Tag(tag_id=1,
            name="playstore app")
        ]
    return tag_dtos


@pytest.fixture()
def post_tag_dtos():
    post_tag_dtos = [
        PostTag(post_id=1,
                tag_id=1)
    ]
    return post_tag_dtos

@pytest.fixture()
def post_tag_details():
    post_tag_details = [
        PostTagDetails(
            tags=tag_dtos,
            post_tag_ids= post_tag_dtos)
        ]
    return post_tag_details

@pytest.fixture()
def post_reactions_count_dto():
    post_reactions_count_dto = PostReactionsCount(post_id=1,
                                                  reactions_count=1)
        
    return post_reactions_count_dto
   

@pytest.fixture()
def comment_reaction_count_dto():
    comment_reaction_count_dto = CommentReactionsCount(comment_id=1,
                                                       reactions_count=1)
    return comment_reaction_count_dto                            
    

@pytest.fixture()
def post_comments_count_dto():
    post_comments_count_dto = PostCommentsCount(post_id=1,
                                                comments_count=1)
    return post_comments_count_dto


@pytest.fixture()
def comment_replies_count_dto():
    comment_replies_count_dto = CommentRepliesCount(comment_id=1,
                                                     replies_count=1)
    return comment_replies_count_dto


@pytest.fixture()
def complete_post_details_dto():
    complete_post_details_dto =  CompletePostDetails(post_dtos=post_dtos,
                    post_reaction_counts=post_reactions_count_dto,
                    comment_reaction_counts=comment_reaction_count_dto,
                    comment_count=post_comments_count_dto,
                    reply_counts=comment_replies_count_dto,
                    comment_dtos=comment_dtos,
                    post_tag_ids=post_tag_dtos,
                    tags=tag_dtos,
                    users_dtos=user_dtos)
                    
    return complete_post_details_dto


