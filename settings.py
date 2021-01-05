import os


class Config(object):
    MYSQL_USER = 'sql12385144'
    MYSQL_PASSWORD = 'idpeHyHtag'
    MYSQL_HOST = 'sql12.freemysqlhosting.net'
    MYSQL_DB = 'sql12385144'
    MYSQL_CURSORCLASS = 'DictCursor'



config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'heroku': HerokuConfig,
    'docker': DockerConfig,
    'unix': UnixConfig,

    'default': DevelopmentConfig
}