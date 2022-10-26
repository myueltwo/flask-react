from api_server_flask.api import create_app
import os

app = create_app(os.getenv("FLASK_ENV", "development"))

if __name__ == '__main__':
    app.run(debug=True)
