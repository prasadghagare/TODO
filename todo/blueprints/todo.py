from . import bp
from flask import render_template, request, make_response, redirect, current_app, g
from ..models import Item, List
from .. import db



@bp.route("/",methods=['GET'])
def index():
    return render_template('index.html')

@bp.route("/lists/the-only-list-in-the-world", methods=['GET'])
def view_list():
    items = Item.query.with_entities(Item.text)
    return render_template('list.html', items = items)

@bp.route("/lists/new", methods =['POST'])
def new_list():

    list_ = List()

    text = Item(text = request.form.get('item_text'), list_if = list_)

    db.session.add(list_)
    db.session.commit()

    return redirect('/lists/the-only-list-in-the-world')
