# -*- coding: utf-8 -*-
"""This file defines the routes and view functions."""
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from . import app
from .forms import LoginForm, SignupForm
from .models import User


@app.route('/')
def hello_world():
    return render_template('hello_world.html', current_user=current_user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        # flash('You are already logged in.')
        return redirect('/')

    form = LoginForm()
    if form.validate_on_submit():  # includes username/password validations
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user)
        # flash('Logged in successfully.')
        return redirect('/')
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        # flash('You are already logged in.')
        return redirect('/')

    form = SignupForm()
    if form.validate_on_submit():  # includes username/password validations
        user = User(username=form.username.data, password=form.password.data).save()
        login_user(user)
        # flash('Signed up successfully.')
        return redirect('/')
    return render_template('signup.html', form=form)


# TODO: create better example for @login_required, since having it
#       on '/logout' is demonstrative but weird
@app.route('/logout')
@login_required
def logout():
    logout_user()
    # flash('Logged out successfully.')
    return redirect('/')
