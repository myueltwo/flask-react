"""Global pytest fixtures."""
import pytest

from api_server_flask.api import create_app
from api_server_flask.api.config import db as database
from api_server_flask.api.models.user import User
from api_server_flask.tests.util import (
    LOGIN,
    PASSWORD,
    create_default_roles,
    ADMIN_LOGIN,
    ADMIN_PASSWORD,
)
import os


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
    create_default_roles(db)
    user = User(
        name="Элина",
        surname="Яхина",
        patronymic="Эльмаровна",
        login=LOGIN,
        password=PASSWORD,
        role_id=os.getenv("ROLE_STUDENT"),
    )
    db.session.add(user)
    db.session.commit()
    return user


@pytest.fixture
def admin(db):
    create_default_roles(db)
    user = User(
        name="Юлия",
        surname="Уразбахтина",
        patronymic="Олеговна",
        login=ADMIN_LOGIN,
        password=ADMIN_PASSWORD,
        role_id=os.getenv("ROLE_DECANAT"),
    )
    db.session.add(user)
    db.session.commit()
    return user
