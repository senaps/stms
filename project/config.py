import os


export_path = os.environ.get('export_path', '/tmp/stms_exports/')
curr_path = os.path.abspath(os.path.curdir)

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


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