"""Class definition for TypeGrade."""
from api_server_flask.api.config import db
from api_server_flask.api.models.util import Base


class TypeGrade(Base):
    """TypeGrade Model for storing grade by type."""

    name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<TypeGrade name={self.name}>"
