from . import bp
from flask import render_template, request, make_response, redirect, current_app, g
from ..models import Item
from .. import db
from sqlite3 import dbapi2 as sqlite3


@bp.route("/",methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print "get me good"
        text = Item(text = request.form.get('item_text'))
        db.session.add(text)
        #db.session.add()
        db.session.commit()
        print "commited"
        return redirect('/')
        #return render_template('index.html',new_item_text = request.form.get('item_text'))
    items = Item.query.with_entities(Item.text)
    print "are htese itms", items
    return render_template('index.html', items = items)

def connect_db():
    rv = sqlite3.connect(current_app.config['DATABASE'])
    rv.row_factory = sqlite3.row_factory
    return rv

def init_db():
    print "Iam Initialized"
    db.create_all()



def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
