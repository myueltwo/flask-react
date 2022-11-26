from api_server_flask.api.config import db, bcrypt
from jwt import (
    encode as encode_jwt,
    decode as decode_jwt,
    ExpiredSignatureError,
    InvalidTokenError,
)
from datetime import datetime, timedelta
from flask import current_app
from api_server_flask.util.result import Result
from api_server_flask.api.models.util import create_id


def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model):
    id = db.Column(db.String(32), primary_key=True, default=create_id())
    name = db.Column(db.String(120), nullable=False)
    surname = db.Column(db.String(120), nullable=False)
    patronymic = db.Column(db.String(120), nullable=False)
    login = db.Column(db.String(20), unique=True, nullable=False)
    # email = db.Column(db.String(60), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)

    role_id = db.Column(db.String(32), db.ForeignKey('role.id'), nullable=False)
    role = db.relationship('Role', backref=db.backref('users', lazy=True))
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
            payload = {"exp": expire, "iat": now, "sub": self.id, "role": self.role_id}
            return encode_jwt(
                payload, current_app.config.get("SECRET_KEY"), algorithm="HS256"
            )
        except Exception as e:
            return e

    @property
    def password(self):
        raise AttributeError("password: write-only field")

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def verify_reset_token(token):
        if isinstance(token, bytes):
            token = token.decode("ascii")
        if token.startswith("Bearer "):
            split = token.split("Bearer")
            token = split[1].strip()
        try:
            payload = decode_jwt(
                token, current_app.config.get("SECRET_KEY"), algorithms=["HS256"]
            )
            from api_server_flask.api.models.black_listed_token import BlacklistedToken

            if BlacklistedToken.check_blacklist(token):
                error = "Token blacklisted. Please log in again."
                return Result.Fail(error)
            return Result.Ok(
                dict(user_id=payload["sub"], token=token, expires_at=payload["exp"],
                     role=payload["role"])
            )
        except ExpiredSignatureError:
            error = "Access token expired. Please log in again."
            return Result.Fail(error)
        except InvalidTokenError:
            error = "Invalid token. Please log in again"
            return Result.Fail(error)

    @classmethod
    def get_by_login(cls, login):
        return cls.query.filter_by(login=login).first()

    @classmethod
    def find_by_id(cls, public_id):
        return cls.query.filter_by(id=public_id).first()

    def __repr__(self):
        return f"<User name={self.name}, login={self.login}>"
