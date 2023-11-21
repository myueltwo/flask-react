"""Class definition for ActivitySubType."""
from api_server_flask.api.config import db
from api_server_flask.api.models.util import Base


class ActivitySubType(Base):
    """ActivitySubType model for sorting type of sub activity"""

    name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<ActivitySubType name={self.name}>"
