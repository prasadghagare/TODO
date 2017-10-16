from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def creat_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    from .blueprints import bp as todo_blueprint
    app.register_blueprint(todo_blueprint)
    return app
