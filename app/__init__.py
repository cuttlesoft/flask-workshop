# -*- coding: utf-8 -*-
"""This file initializes the application."""
from flask import Flask

app = Flask(__name__)

from . import views
