"""Class definition for Lab."""
from api_server_flask.api.config import db
from api_server_flask.api.models.util import Base


class Lab(Base):
    name = db.Column(db.String(120), nullable=False)
    subject_id = db.Column(db.String(32), db.ForeignKey("subject.id"), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return (
            f"<Lab name={self.name} subject_id={self.subject_id} "
            f"deadline={self.deadline}>"
        )
