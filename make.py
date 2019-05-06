import os
from project.extentions import db
from app import app
from project.config import export_path

with app.app_context():
    db.create_all()

if not os.path.isdir(export_path):
    os.makedirs(export_path)

