"""Class definition for Role."""
from api_server_flask.api.config import db
from api_server_flask.api.models.util import Base


class Role(Base):
    """Role Model for storing roles of users."""

    name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<Role name={self.name}>"

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
