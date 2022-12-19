"""Class definition for GradeUsers."""
from api_server_flask.api.config import db
from api_server_flask.api.models.util import Base


class GradeUsers(Base):
    """GradeUsers Model for storing grade of users."""

    user_id = db.Column(db.String(32), db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", backref=db.backref("user", lazy=True))
    grade_id = db.Column(db.String(32), db.ForeignKey("grade.id"), nullable=False)
    grade = db.relationship("Grade", backref=db.backref("grade_users", lazy=True))
    value = db.Column(db.Integer, default=0)

    def __repr__(self):
        return (
            f"<GradeUsers user_name={self.user.surname} value={self.value}"
            f" subject={self.grade.subject.name}>"
        )
