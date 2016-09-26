# -*- coding: utf-8 -*-
"""This file defines the routes and view functions."""
from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from . import app
from .models import User


@app.route('/')
def hello_world():
    return render_template('hello_world.html', current_user=current_user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('hello_world'))

    # For GET request, render login form
    if request.method == 'GET':
        return render_template('login.html')

    # For POST request, find user and try to log them in
    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(request.form.get('password')):
        login_user(user)
        return redirect(url_for('hello_world'))

    return 'Invalid login. <a href="%s">Go back?</a>' % url_for('login')


# TODO: create better example for @login_required, since having it
#       on '/logout' is demonstrative but weird
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out. <a href="%s">Log in?</a>' % url_for('login')
