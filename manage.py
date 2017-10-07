from todo import creat_app
from todo import db
from todo.models import Item
import os

app = creat_app(os.getenv('FLASK_CONFIG') or 'default')
