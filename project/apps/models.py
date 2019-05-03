import time

from ..extentions import db
from ..utils import get_current_timestamp

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    detail = db.Column(db.Text)
    post_date = db.Column(db.Integer, default=get_current_timestamp())
    edit_date = db.Column(db.Integer)
    published = db.Column(db.Boolean, default=True)
    generated = db.Column(db.Boolean, default=False)
