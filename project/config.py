import os


export_path = os.environ.get('export_path', '/tmp/stms_exports/')
curr_path = os.path.abspath(os.path.curdir)
upload_path = os.path.join(curr_path, "project/media/images/")

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SEND_FILE_MAX_AGE_DEFAULT = 0

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/stms.db'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('db')


class TestingConfig(Config):
    TESTING = True


def get_conf(conf_name):
    configs = {
        'develop': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig
        }
    return configs[conf_name]