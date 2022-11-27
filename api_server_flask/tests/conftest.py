"""Global pytest fixtures."""
import pytest

from api_server_flask.api import create_app
from api_server_flask.api.config import db as database
from api_server_flask.api.models.user import User
from api_server_flask.api.models.role import Role
from api_server_flask.tests.util import LOGIN, PASSWORD
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
    role_student = Role(id=os.getenv("ROLE_STUDENT"), name="Студент")
    role_tutor = Role(id=os.getenv("ROLE_TUTOR"), name="Преподаватель")
    role_deans_office = Role(id=os.getenv("ROLE_DECANAT"), name="Деканат")
    db.session.add_all([role_student, role_tutor, role_deans_office])
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
