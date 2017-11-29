
class Config(object):
    """
    Common configurations
    """


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True

app_config = {
    'development': DevelopmentConfig
}