from .query_handler import (get_post_by_title, get_post_byid, mark_as_gen,
                            insert_post, edit_post, remove_post,
                            get_paginated_posts, get_fresh_posts)
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


def add_post_handler(title, detail, thumb):
    if get_post_by_title(title=title):
        raise AlreadyExists("post with this title already in db")
    insert_post(title=title, detail=detail, thumb=thumb)
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


def generate_handle():
    from .generate_helpers import render_template, zip_file_func, copy_blank_media
    from ..config import export_path, curr_path

    posts = get_fresh_posts()
    mark_as_gen(posts=posts)
    copy_blank_media(dir_path=export_path, curr_path=curr_path)
    render_template(posts=posts, export_path=export_path)
    file_path = zip_file_func(dir_path=export_path)
    return file_path



