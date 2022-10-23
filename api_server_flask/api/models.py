from api_server_flask.api.config import db, bcrypt
from jwt import encode as encode_jwt, decode as decode_jwt, ExpiredSignatureError, InvalidTokenError
from flask_login import UserMixin
from datetime import datetime, timedelta
from flask import flash, current_app
import uuid


def create_id():
    return uuid.uuid4().hex


def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    surname = db.Column(db.String(120), nullable=False)
    patronymic = db.Column(db.String(120), nullable=False)
    login = db.Column(db.String(20), unique=True, nullable=False)
    # email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    # role_id = db.Column(db.String(32), db.ForeignKey('role.id'), nullable=False)
    # role = db.relationship('Role', backref=db.backref('users', lazy=True))
    # group_id = db.Column(db.String(32), db.ForeignKey('group.id'), nullable=True)

    def encode_access_token(self):
        """
           Generates the Auth Token
           :return: string
           """
        try:
            now = datetime.utcnow()
            token_age_h = current_app.config.get("TOKEN_EXPIRE_HOURS")
            token_age_m = current_app.config.get("TOKEN_EXPIRE_MINUTES")
            expire = now + timedelta(hours=token_age_h, minutes=token_age_m)
            if current_app.config["TESTING"]:
                expire = now + timedelta(seconds=5)
            payload = {
                'exp': expire,
                'iat': now,
                'sub': self.id
            }
            return encode_jwt(
                payload,
                current_app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def save(self):
        self.id = create_id()
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def verify_reset_token(token):
        try:
            user_id = decode_jwt(token, current_app.config.get('SECRET_KEY'), algorithms=["HS256"])['sub']
            return User.query.get(user_id)
        except ExpiredSignatureError:
            flash('Signature expired. Please log in again.')
            return None
        except InvalidTokenError as e:
            flash('Invalid token. Please log in again')
            return e

    @classmethod
    def get_by_login(cls, login):
        return cls.query.filter_by(login=login).first()

    def __repr__(self):
        return "User('{self.name}', 'self.login')"
