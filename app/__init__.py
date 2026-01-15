import os
from flask import Flask
from app.config import Config, TestingConfig
from app.db import db
from app.routes import bp


def create_app(testing: bool = False):
    app = Flask(
        __name__,
        static_folder=os.path.join(os.getcwd(), "static")
    )

    if testing:
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(bp)

    return app