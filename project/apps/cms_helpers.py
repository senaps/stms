from .query_hanler import (get_post_by_title, get_post_byid,
                           insert_post, edit_post, remove_post,
                           get_paginated_posts)
from ..utils.error_helpers import AlreadyExists


def get_all_posts_handler(page, weight):
    posts = get_paginated_posts(page, weight)
    if not posts:
        raise ValueError("no posts in the db")
    return posts


def get_post_handler(id):
    post_obj = get_post_byid(id=id)
    if not post_obj:
        raise ValueError("no post with that id exists")
    return post_obj


def add_post_handler(title, detail):
    if get_post_by_title(title=title):
        raise AlreadyExists("post with this title already in db")
    insert_post(title=title, detail=detail)
    return True


def edit_post_handler(id, title, detail, generated, published):
    post_obj = get_post_byid(id=id)
    if not post_obj:
        raise ValueError("no post with that id exists")
    edit_post(post_obj=post_obj, title=title, detail=detail,
              generated=generated, published=published)
    return True


def remove_post_handler(id):
    post_obj = get_post_byid(id=id)
    if not post_obj:
        raise ValueError("no post with that id exists")
    remove_post(post_obj=post_obj)
    return True
