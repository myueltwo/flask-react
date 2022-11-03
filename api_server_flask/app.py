from api_server_flask.api import create_app, db
from api_server_flask.api.models.user import User
from api_server_flask.api.models.black_listed_token import BlacklistedToken
import os

app = create_app(os.getenv("FLASK_ENV", "development"))

if __name__ == '__main__':
    app.run(debug=True)


@app.shell_context_processor
def shell():
    return {"db": db,
            "User": User,
            "BlacklistedToken": BlacklistedToken
            }
