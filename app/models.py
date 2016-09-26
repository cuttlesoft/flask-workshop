# -*- coding: utf-8 -*-
"""This file defines the database models."""
from werkzeug.security import generate_password_hash, check_password_hash

from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)

    # The following password setup was pulled directly
    # from Fbone (a Flask boilerplate application)

    _password = db.Column('password', db.String(200), nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self, password):
        if self.password is None:
            return False
        return check_password_hash(self.password, password)
