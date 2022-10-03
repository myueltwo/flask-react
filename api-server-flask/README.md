# Server side setup
## Freeze flask dependencies
    cd api-server-flask
    pip freeze > requirements.txt
## Create environment
```
    cd api-server-flask
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
## quick start
```
    set FLASK_APP=app.py
    set FLASK_ENV=development
    py -m flask run
```