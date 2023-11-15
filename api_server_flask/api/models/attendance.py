"""Class definition for Attendance."""
from api_server_flask.api.config import db
from api_server_flask.api.models.util import Base
from datetime import datetime


class Attendance(Base):
    """Attendance model for sorting attendances"""

    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    subject_id = db.Column(db.String(32), db.ForeignKey("subject.id"), nullable=False)
    group_id = db.Column(db.String(32), db.ForeignKey("group.id"), nullable=False)
    group = db.relationship("Group", backref=db.backref("attendance", lazy="dynamic"))
    type_id = db.Column(
        db.String(32), db.ForeignKey("attendance_type.id"), nullable=False
    )
    type = db.relationship("AttendanceType", backref=db.backref("attendance", lazy=True))

    def __repr__(self):
        return f"<Attendance group={self.group.name} type={self.type.name}>"
