import sqlalchemy as sa
import sqlalchemy.orm as so

from flask_tutorial import app, db
from flask_tutorial.models import Post, User


@app.shell_context_processor
def make_shell_context():
    return {
        "sa": sa,
        "so": so,
        "db": db,
        "User": User,
        "Post": Post,
    }
