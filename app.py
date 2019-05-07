import os

from project.application import create_app

conf = os.environ.get('conf', 'develop')
app = create_app(conf_name=conf)
