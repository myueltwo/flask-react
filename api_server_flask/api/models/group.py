"""Class definition for Group."""
from api_server_flask.api.config import db
from api_server_flask.api.models.util import Base


class Group(Base):
    name = db.Column(db.String(120), nullable=False)
    users = db.relationship("User", backref="group", lazy="dynamic")

    def __repr__(self):
        return f"<Group name={self.name}>"
