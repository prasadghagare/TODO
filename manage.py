from todo import creat_app
from todo import db
from todo.models import Item
import os

app = creat_app(os.getenv('FLASK_CONFIG') or 'default')


def register_cli(app):
    @app.cli.command('initdb')
    def initdb_command():
        """Creates the database tables."""
        init_db()
        print('Initialized the database.')

def init_db():
    print "Iam Initialized"
    db.create_all()

register_cli(app)
