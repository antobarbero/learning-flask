import os

from flask import Flask

from . import db, auth


def create_app(test_config=None):
    """Application factory function that creates and configures the app."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',  # TODO: override with a random value when deploying
        # store db in instance directory
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # override default configuration with values taken from config.py
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config
        app.config.update(test_config)

    try:
        os.makedirs(app.instance_path)  # ensure the instance folder exists
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello world!'

    db.init_app(app)  # register db commands

    app.register_blueprint(auth.bp)  # register blueprint

    return app
