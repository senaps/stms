from flask import Blueprint, request, jsonify, render_template

from .cms_helpers import (add_post_handler, edit_post_handler,
                          remove_post_handler, get_post_handler,
                          get_all_posts_handler)
from ..utils.error_helpers import AlreadyExists


cms = Blueprint("cms", __name__, url_prefix="/cms")


def make_response(data=None, status_code=200, header=None):
    return jsonify({"result": data}), status_code, header


@cms.route("/")
@cms.route("/<page>/")
@cms.route("/<page>/<weight>/")
def index_route(page=1, weight=20):  # list posts
    try:
        return render_template("index.html")
        result = get_all_posts_handler(page=page, weight=weight)
    except:
        raise


@cms.route("/add/")
@cms.route("/edit/<id>")
def edit_post(id=None):  # edit or add a new post form!
    try:
        if id:
            post = get_post_handler(id=id)
            if not post:
                return "no post with that id! 204"
            return post.title
    except ValueError:
        return "no post with that id 204!"
    except:
        raise


@cms.route("/post/", methods=['POST'])
def add_post_route():
    try:
        data = request.get_json()
        title = data.get('title')
        detail = data.get('detail')
        add_post_handler(title=title, detail=detail)
        return make_response(status_code=201)
    except AlreadyExists:
        header = {"message": "title already exists in the system"}
        return make_response(status_code=409, header=header)
    except:
        raise


@cms.route("/post/<id>/", methods=['PUT'])
def edit_post_route(id):
    try:
        data = request.get_json()
        title = data.get('title')
        detail = data.get('detail')
        publish = data.get('published')
        generated = data.get('generated')
        edit_post_handler(id=id, title=title, detail=detail,
                          generated=generated, published=publish)
        return make_response(status_code=202)
    except ValueError:
        header = {"message": "no post with that id"}
        return make_response(status_code=204, header=header)
    except:
        raise


@cms.route("/post/<id>/", methods=['DELETE'])
def remove_post_route(id):
    try:
        remove_post_handler(id=id)
        return "removed! 202"
    except ValueError:
        header = {"message": "no post with that id"}
        return make_response(status_code=204, header=header)
    except:
        raise