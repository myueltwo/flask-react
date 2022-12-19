from api_server_flask.api import create_app, db
from api_server_flask.api.models.user import User
from api_server_flask.api.models.black_listed_token import BlacklistedToken
from api_server_flask.api.models.role import Role
from api_server_flask.api.models.group import Group
from api_server_flask.api.models.subject import Subject
from api_server_flask.api.models.type_grade import TypeGrade
from api_server_flask.api.models.grade import Grade
from api_server_flask.api.models.grade_users import GradeUsers
import os
import click
from api_server_flask.api.models.util import create_id
from sqlalchemy.exc import DatabaseError

app = create_app(os.getenv("FLASK_ENV", "development"))


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "User": User,
        "BlacklistedToken": BlacklistedToken,
        "Role": Role,
        "Group": Group,
        "Subject": Subject,
        "TypeGrade": TypeGrade,
        "Grade": Grade,
        "GradeUsers": GradeUsers,
    }


@app.cli.command("add-default-roles", short_help="Add default roles")
def add_default_roles():
    """Add default roles to database"""
    role_student = Role(id=os.getenv("ROLE_STUDENT", create_id()), name="Студент")
    role_tutor = Role(id=os.getenv("ROLE_TUTOR", create_id()), name="Преподаватель")
    role_deans_office = Role(id=os.getenv("ROLE_DECANAT", create_id()), name="Деканат")
    try:
        db.session.add_all([role_tutor, role_student, role_deans_office])
        db.session.commit()
        message = "Successfully added default roles"
        click.secho(message, fg="blue", bold=True)
        return 0
    except DatabaseError:
        error = "Error: the roles are already exist"
        click.secho(f"{error}\n", fg="red", bold=True)
        return 1


@app.cli.command("add-user", short_help="Add a new user")
@click.argument("login")
@click.option(
    "--name",
    required=True,
    nargs=3,
    type=str,
    help="Surname/Name/Patronymic of new user",
)
@click.option(
    "--admin",
    "role",
    flag_value="admin",
    help="New user has administrator/dean's office role",
)
@click.option(
    "--tutor",
    "role",
    flag_value="tutor",
    help="New user has tutor role",
)
@click.option(
    "--student",
    "role",
    default=True,
    flag_value="student",
    help="New user has student role",
)
@click.password_option(help="Do not set password on the command line!")
def add_user(login, name, role, password):
    """Add a new user to the database with login = LOGIN."""
    if User.get_by_login(login):
        error = f"Error: {login} is already registered"
        click.secho(f"{error}\n", fg="red", bold=True)
        return 1
    if role == "admin":
        role_id = os.getenv("ROLE_DECANAT")
    elif role == "tutor":
        role_id = os.getenv("ROLE_TUTOR")
    else:
        role_id = os.getenv("ROLE_STUDENT")
    surname, name_user, patronymic = name
    new_user = User(
        name=name_user,
        surname=surname,
        patronymic=patronymic,
        login=login,
        password=password,
        role_id=role_id,
    )
    db.session.add(new_user)
    db.session.commit()
    message = f"Successfully added new {role} user:\n {new_user}"
    click.secho(message, fg="blue", bold=True)
    return 0
