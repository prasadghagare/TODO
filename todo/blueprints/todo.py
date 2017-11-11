from . import bp
from flask import render_template, request, make_response, redirect, current_app, g
from ..models import Item, List
from .. import db
from sqlalchemy.orm import joinedload


@bp.route("/",methods=['GET'])
def index():
    return render_template('index.html')

@bp.route("/lists/<int:list_id>", methods=['GET'])
def view_list(list_id):

    items = Item.query.with_entities(Item.text).filter_by(list_id = list_id).all()
    return render_template('list.html', items = items, list_id = list_id)

@bp.route("/lists/new", methods =['POST'])
def new_list():

    list_ = List()
    text = Item(text = request.form.get('item_text'), list_if = list_)

    db.session.add(list_)
    db.session.commit()
    list_id = list_.list_id
    return redirect('/lists/'+ str(list_id))

@bp.route("/lists/<int:list_id>/add_item", methods = ['POST'])
def add_item(list_id):

    query = List.query.options(joinedload('listar'))
    for i in query:
        if i.list_id == list_id:
            text = Item(text = request.form.get('item_text'), list_if = i)
            db.session.add(i)
            db.session.commit()
    return redirect('/lists/'+ str(list_id))
