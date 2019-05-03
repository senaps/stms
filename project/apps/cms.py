from flask import (Blueprint, request, jsonify, send_file,
                   render_template, redirect, url_for)

from .cms_helpers import (add_post_handler, edit_post_handler,
                          remove_post_handler, get_post_handler,
                          get_all_posts_handler, generate_handle)
from ..utils.error_helpers import AlreadyExists


cms = Blueprint("cms", __name__, url_prefix="/cms")


def make_response(data=None, status_code=200, header=None):
    return jsonify({"result": data}), status_code, header


@cms.route("/")
@cms.route("/<page>/")
@cms.route("/<page>/<weight>/")
def index_route(page=1, weight=20):  # list posts
    try:
        result = get_all_posts_handler(page=page, weight=weight)
        return render_template("dash.html", posts=result)
    except:
        raise


@cms.route("/add/")
def add_post():  # edit or add a new post form!
    try:
        return render_template("add.html")
    except ValueError:
        return "no post with that id 204!"
    except:
        raise


@cms.route("/edit/<id>")
def edit_post(id=None):  # edit or add a new post form!
    try:
        post = get_post_handler(id=id)
        if not post:
            return "no post with that id! 204"
        return render_template("edit.html", post=post)
    except ValueError:
        return "no post with that id 204!"
    except:
        raise


@cms.route("/post/", methods=['POST'])
def add_post_route():
    try:
        title = request.form.get('title')
        detail = request.form.get('detail')
        add_post_handler(title=title, detail=detail)
        return redirect(url_for('cms.index_route'))
    except AlreadyExists:
        header = {"message": "title already exists in the system"}
        return make_response(status_code=409, header=header)
    except:
        raise


@cms.route("/post/<id>/edit/", methods=['POST'])
def edit_post_route(id):
    try:
        title = request.form.get('title')
        detail = request.form.get('detail')
        publish = request.form.get('published')
        generated = request.form.get('generated')
        edit_post_handler(id=id, title=title, detail=detail,
                          generated=generated, published=publish)
        return redirect(url_for('cms.index_route'))
    except ValueError:
        return redirect(url_for('cms.edit_post', id=id))
    except:
        raise


@cms.route("/post/<id>/remove/")
def remove_post_route(id):
    try:
        remove_post_handler(id=id)
        return redirect(url_for('cms.index_route'))
    except ValueError:
        return redirect(url_for('cms.index_route'))
    except:
        raise


@cms.route("/generate/")
def generate_route():
    try:
        filename = generate_handle()
        return send_file(filename, as_attachment=True)
    except:
        raise
