# Server side setup
## Freeze flask dependencies
    cd api_server_flask
    pip freeze > requirements.txt
## Create environment
```
    cd api_server_flask
    py -3 -m venv venv
```
## Activate the environment
```
    venv\Scripts\activate
```
## Installation
```
   pip3 install -r requirements.txt
```
## Create Database
```
    flask shell
    from api import db
    db.create_all()
```
## Update Database
```
    flask db init
    flask db migrate --message "some message for action"
    flask db upgrade
``` 
## quick start
```
    set FLASK_APP=app.py
    set FLASK_ENV=development
    py -m flask run
```
