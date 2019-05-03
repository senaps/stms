from flask import Blueprint

cms = Blueprint("cms", __name__, url_prefix="/cms")

@cms.route("/")
def index_route():
    return "hello world!"