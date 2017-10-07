from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from todo.blueprints.todo import init_db

print "I was run"
def creat_app():
    #app.config.update(config or {})
    print "me too"
    app = Flask('todo')
    #app.config.update(config or {})
    #db = SQLAlchemy(app)
    register_cli(app)

    from todo.blueprints import bp
    app.register_blueprint(bp)

    return app

def register_cli(app):
    @app.cli.command('initdb')
    def initdb_command():
        """Creates the database tables."""
        init_db()
        print('Initialized the database.')
