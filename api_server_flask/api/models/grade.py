"""Class definition for Grade."""
from api_server_flask.api.config import db
from api_server_flask.api.models.util import Base
from datetime import datetime


class Grade(Base):
    """Grade Model for storing grade."""

    subject_id = db.Column(db.String(32), db.ForeignKey("subject.id"), nullable=False)
    subject = db.relationship("Subject", backref=db.backref("grade", lazy=True))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    type_id = db.Column(db.String(32), db.ForeignKey("type_grade.id"), nullable=False)
    type = db.relationship("TypeGrade", backref=db.backref("grade", lazy=True))

    def __repr__(self):
        return f"<Grade type={self.type.name} subject={self.subject.name}>"
