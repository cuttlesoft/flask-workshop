# -*- coding: utf-8 -*-
"""This file initializes the application."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = 'ThisKeyIsTheMostSecretOfAllKeys'

# Database setup with Flask-SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # suppress warning

db = SQLAlchemy(app)

# User session management with Flask-Login

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


from . import views
