from api_server_flask.api import create_app, db
from api_server_flask.api.models.user import User
from api_server_flask.api.models.black_listed_token import BlacklistedToken
from api_server_flask.api.models.role import Role
import os

app = create_app(os.getenv("FLASK_ENV", "development"))


@app.shell_context_processor
def shell():
    return {"db": db, "User": User, "BlacklistedToken": BlacklistedToken, "Role": Role}
