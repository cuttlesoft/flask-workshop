# -*- coding: utf-8 -*-
"""This file initializes the application."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

# Flask-Login

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


from . import views
