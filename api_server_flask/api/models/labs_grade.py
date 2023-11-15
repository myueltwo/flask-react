"""Class definition for LabsGrade."""
from api_server_flask.api.config import db
from api_server_flask.api.models.util import Base
from datetime import datetime


class LabsGrade(Base):
    lab_id = db.Column(db.String(32), db.ForeignKey("lab.id"), nullable=False)
    lab = db.relationship("Lab", backref=db.backref("labs_grade", lazy=True))
    user_id = db.Column(db.String(32), db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", backref=db.backref("labs_grade", lazy=True))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return (
            f"<LabsGrade user={self.user.surname} lab={self.lab.name} date={self.date}>"
        )
