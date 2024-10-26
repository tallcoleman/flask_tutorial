from flask import render_template, flash, redirect, url_for
from flask_tutorial import app
from flask_tutorial.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Ben"}
    posts = [
        {
            "author": {"username": "John"},
            "body": "Beautiful day in Portland!",
        },
        {
            "author": {"username": "Susan"},
            "body": "The Avengers movie was so cool!",
        },
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login requested for {form.username.data}, remember_me={
              form.remember_me.data}")
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)
