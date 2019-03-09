import os

from flask import Flask


def create_app(test_config=None):
    """Application factory function that creates and configures the app.
    """
    app = Flask('__name__', instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',  # TODO: override with a random value when deploying
        DATABASE=os.path.join(app.instance_path, 'flask.sqlite')
    )

    if test_config is None:
        # override default configuration with values taken from config.py
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)  # ensure the instance folder exists
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello world!'

    return app
