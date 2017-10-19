from . import bp
from flask import render_template, request, make_response, redirect, current_app, g
from ..models import Item
from .. import db



@bp.route("/",methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print "get me good"
        text = Item(text = request.form.get('item_text'))
        db.session.add(text)
        #db.session.add()
        db.session.commit()
        print "commited"
        return redirect('/lists/the-only-list-in-the-world')
        #return render_template('index.html',new_item_text = request.form.get('item_text'))
    items = Item.query.with_entities(Item.text)
    print "are htese itms", items
    return render_template('index.html', items = items)

@bp.route("/lists/the-only-list-in-the-world", methods=['GET'])
def view_list():
    items = Item.query.with_entities(Item.text)
    return render_template('list.html', items = items)
