"""Class definition for AttendanceType."""
from api_server_flask.api.config import db
from api_server_flask.api.models.util import Base


class AttendanceType(Base):
    """AttendanceType model for sorting type of attendances"""

    name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<AttendanceType name={self.name}>"
