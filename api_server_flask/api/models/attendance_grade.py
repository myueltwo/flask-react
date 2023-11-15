"""Class definition for AttendanceGrade."""
from api_server_flask.api.config import db
from api_server_flask.api.models.util import Base


class AttendanceGrade(Base):
    """AttendanceGrade model for sorting grades of attendance"""

    user_id = db.Column(db.String(32), db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", backref=db.backref("attendance_grade", lazy=True))
    attendance_id = db.Column(
        db.String(32), db.ForeignKey("attendance.id"), nullable=False
    )
    attendance = db.relationship(
        "Attendance", backref=db.backref("attendance_grade", lazy=True)
    )
    active = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<AttendanceGrade user={self.user.surname} active={self.active} attendance={self.attendance_id}>"
