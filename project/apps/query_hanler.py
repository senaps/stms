from .models import db, Post


def get_paginated_posts(page, weight):
    return Post.query.paginate(page=page, per_page=weight, error_out=False)


def get_fresh_posts():
    return Post.query.filter_by(generated=False).all()


def get_post_byid(id):
    return Post.query.filter_by(id=id).first()


def get_post_by_title(title):
    return Post.query.filter_by(title=title).first()


def insert_post(title, detail, published=True, generated=False):
    try:
        new_entry = Post(title=title, detail=detail, published=published,
                         generated=generated)
        db.session.add(new_entry)
        db.session.commit()
        return True
    except:
        raise


def edit_post(post_obj, title, detail, published, generated):
    try:
        if title and post_obj.title != title:
            post_obj.title = title
        if detail and post_obj.detail != detail:
            post_obj.detail = detail
        if published is not None and post_obj.published != published:
            post_obj.published = published
        if generated is not None and post_obj.generated != generated:
            post_obj.generated = generated
        db.session.commit()
        return True
    except:
        db.session.rollback()
        raise


def mark_as_gen(posts):
    for post in posts:
        post.generated = True
    db.session.commit()


def remove_post(post_obj):
    try:
        db.session.delete(post_obj)
        db.session.commit()
        return True
    except:
        raise