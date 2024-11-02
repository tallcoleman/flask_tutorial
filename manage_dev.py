import os
from datetime import datetime, timedelta, timezone

from flask_tutorial import app, db
from flask_tutorial.models import User, Post

os.environ["DATABASE_URL"] = "sqlite://"


def set_up():
    app_context = app.app_context()
    app_context.push()

    db.drop_all()
    db.create_all()

    add_data()

    db.session.remove()
    app_context.pop()


def add_data():
    # set up the users
    u1 = User(username="susan", email="susan@example.com")
    u1.set_password("cat")
    u2 = User(username="john", email="john@example.com")
    u2.set_password("dog")
    u3 = User(username="mary", email="mary@example.com")
    u3.set_password("mouse")
    u4 = User(username="david", email="david@example.com")
    u4.set_password("bird")
    db.session.add_all([u1, u2, u3, u4])
    db.session.commit()

    # set up the followers
    u1.follow(u2)  # john follows susan
    u1.follow(u4)  # john follows david
    u2.follow(u3)  # susan follows mary
    u3.follow(u4)  # mary follows david
    db.session.commit()

    # set up the posts
    now = datetime.now(timezone.utc)
    p1 = Post(
        body="post from john",
        author=u1,
        timestamp=now + timedelta(seconds=1),
    )
    p2 = Post(
        body="post from susan",
        author=u2,
        timestamp=now + timedelta(seconds=4),
    )
    p3 = Post(
        body="post from mary",
        author=u3,
        timestamp=now + timedelta(seconds=3),
    )
    p4 = Post(
        body="post from david",
        author=u4,
        timestamp=now + timedelta(seconds=2),
    )
    db.session.add_all([p1, p2, p3, p4])
    db.session.commit()


if __name__ == "__main__":
    set_up()
