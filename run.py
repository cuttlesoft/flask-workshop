# -*- coding: utf-8 -*-
"""This file is invoked to run the server."""
from app import app, db, models


if __name__ == '__main__':
    db.create_all()

    # TODO: add signup form to create users; default user for now
    if not models.User.query.filter_by(username='TestUser').first():
        user = models.User(username='TestUser')
        user.password = 'testpassword'
        user.save()

    app.run(debug=True)
