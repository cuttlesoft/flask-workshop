# -*- coding: utf-8 -*-
"""This file creates the application's forms."""
from flask_wtf import Form
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import Length, Required

from config import USERNAME_MIN, USERNAME_MAX, PASSWORD_MIN, PASSWORD_MAX
from .models import User


USERNAME_LENGTH = Length(USERNAME_MIN, USERNAME_MAX)
PASSWORD_LENGTH = Length(PASSWORD_MIN, PASSWORD_MAX)


class LoginForm(Form):
    username = StringField('Username', validators=[Required(), USERNAME_LENGTH])
    password = PasswordField('Password', validators=[Required(), PASSWORD_LENGTH])
    submit = SubmitField('Log In')

    def validate_username(self, field):
        """Check whether user exists and given password matches."""
        user = User.query.filter_by(username=field.data).first()
        if not (user and user.check_password(self.password.data)):
            raise ValidationError('Invalid username and/or password.')


class SignupForm(Form):
    username = StringField('Username', validators=[Required(), USERNAME_LENGTH])
    password = PasswordField('Password', validators=[Required(), PASSWORD_LENGTH])
    submit = SubmitField('Sign Up')

    def validate_username(self, field):
        """Check whether username already exists; raise ValidationError if so."""
        if User.query.filter_by(username=field.data).first() is not None:
            raise ValidationError('Username already exists.')
