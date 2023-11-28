"""Class definition for RateActivity."""
from api_server_flask.api.config import db
from api_server_flask.api.models.util import Base


class RateActivity(Base):
    """RateActivity model for sorting type of sub activity"""

    value = db.Column(db.Integer, default=0)
    activity_type_id = db.Column(
        db.String(32), db.ForeignKey("activity_type.id"), nullable=False
    )
    type = db.relationship("ActivityType", backref=db.backref("rate", lazy=True))
    activity_sub_type_id = db.Column(
        db.String(32), db.ForeignKey("activity_sub_type.id"), nullable=True
    )
    sub_type = db.relationship("ActivitySubType", backref=db.backref("rate", lazy=True))

    def __repr__(self):
        return (
            f"<RateActivity name={self.name} type={self.type.name} "
            f"sub_type={self.sub_type.name}>"
        )
