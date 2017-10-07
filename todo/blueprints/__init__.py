from flask import Blueprint, render_template

bp = Blueprint('todo', __name__)

from . import todo
