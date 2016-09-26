# -*- coding: utf-8 -*-
"""This file initializes the application."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # suppress warning

db = SQLAlchemy(app)

from . import views
