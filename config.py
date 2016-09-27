# -*- coding: utf-8 -*-
"""This file contains the application's configuration."""

SECRET_KEY = 'this-key-is-the-most-secret-key'

# Flask-SQLAlchemy

SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Flask-WTF

WTF_CSRF_ENABLED = True

# Miscellaneous

USERNAME_MIN = 4
USERNAME_MAX = 20
PASSWORD_MIN = 8
PASSWORD_MAX = 30
