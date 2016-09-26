# -*- coding: utf-8 -*-
"""This file defines the routes and view functions."""
from flask import render_template

from . import app

@app.route('/')
def hello_world():
    return render_template('hello_world.html')
