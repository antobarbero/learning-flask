"""
setup functions.
"""

import os
import tempfile

import pytest

from flaskr import create_app
from flaskr.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    # creates and opens a temporary file,
    # returning the file object and the path to it.
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,  # tells Flask that the app in in test mode.
        'DATABASE': db_path  # override database path temporarily.
    })

    with app.app_context():
        init_db()  # create db tables.
        get_db().executescript(_data_sql)  # insert data.

    yield app

    os.close(db_fd)  # close db temporary file.
    os.unlink(db_path)  # remove db temporary file.


@pytest.fixture
def client(app):
    """
    To be used for tests to make requests to the application without
    running the server.
    """
    return app.test_client()  # app object created by the app fixture


@pytest.fixture
def runner(app):
    """
    Creates a runner that can call the Click commands registered with the
    application.
    """
    return app.test_cli_runner()
