"""Class definition for Subject."""

from api_server_flask.api.config import db
from api_server_flask.api.models.util import Base


class Subject(Base):
    """Subject Model for storing subjects."""

    name = db.Column(db.String(20), nullable=False)
    count_hours = db.Column(db.Integer, nullable=False)
    labs = db.relationship('Lab', backref='subject', lazy=True)
    # attendance = db.relationship('Attendance', backref='subject', lazy=True)

    def __repr__(self):
        return f"<Subject name={self.name}>"
