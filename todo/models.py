#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()

from . import db


class Item(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)

    text = db.Column(db.String(80), unique=False)

    def __init__(self, text):

        self.text = text

    def __repr__(self):
        return '%s' % self.text
