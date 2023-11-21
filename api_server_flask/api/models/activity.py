"""Class definition for Activity."""
from api_server_flask.api.config import db
from api_server_flask.api.models.util import Base


class Activity(Base):
    """Activity model for users"""

    name = db.Column(db.String(60), nullable=False)
    user_id = db.Column(db.String(32), db.ForeignKey('user.id'), nullable=False)
    file = db.Column(db.String(20), nullable=False)
    status = db.Column(db.Boolean, nullable=True)
    comment = db.Column(db.String(240), nullable=True)
    type_id = db.Column(db.String(32), db.ForeignKey('activity_type.id'), nullable=False)
    rate_id = db.Column(db.String(32), db.ForeignKey('rate_activity.id'), nullable=False)
    rate = db.relationship('RateActivity',
                           backref=db.backref('activity', lazy=True))

    def __repr__(self):
        return f"<Activity name={self.name} rate={self.rate.value} user_id={self.user_id}>"
