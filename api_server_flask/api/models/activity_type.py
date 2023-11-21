"""Class definition for ActivityType."""
from api_server_flask.api.config import db
from api_server_flask.api.models.util import Base


class ActivityType(Base):
    """ActivityType model for sorting type of activity"""

    name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<ActivityType name={self.name}>"
