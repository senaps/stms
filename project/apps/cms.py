from flask import Blueprint

cms = Blueprint("cms", __name__, url_prefix="/cms")


@cms.route("/")
def index_route():
    return "hello world!"


@cms.route("/newpost/")
@cms.route("/newpost/<id>")
def new_post_route(id=None):
    return "create a new post"


@cms.route("/newpost/", methods=['POST'])
def add_post_route():
    return "add a new post to the db"


@cms.route("/newpost/<id>/", methods=['PUT'])
def edit_post_route(id):
    return "edit a post"


@cms.route("/newpost/<id>/", methods=['DELETE'])
def remove_post_route(id):
    return "remove a post"