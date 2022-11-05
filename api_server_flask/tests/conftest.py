"""Global pytest fixtures."""
import pytest

from api_server_flask.api import create_app
from api_server_flask.api.config import db as database
from api_server_flask.api.models.user import User
from api_server_flask.tests.util import LOGIN, PASSWORD


@pytest.fixture
def app():
    app = create_app("testing")
    return app


@pytest.fixture
def db(app, client, request):
    database.drop_all()
    database.create_all()
    database.session.commit()

    def fin():
        database.session.remove()

    request.addfinalizer(fin)
    return database


@pytest.fixture
def user(db):
    user = User(
        name="Элина",
        surname="Яхина",
        patronymic="Эльмаровна",
        login=LOGIN,
        password=PASSWORD,
    )
    db.session.add(user)
    db.session.commit()
    return user
