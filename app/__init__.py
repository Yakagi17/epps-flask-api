import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from  import Bootstrap
from settings import config


bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)


    return app



