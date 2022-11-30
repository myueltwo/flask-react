import uuid
from api_server_flask.api.config import db


def create_id():
    return uuid.uuid4().hex


class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.String(32), primary_key=True, default=lambda: create_id())
