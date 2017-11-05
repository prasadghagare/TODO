from . import db


class Item(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)

    text = db.Column(db.String(80), unique=False)
    list_id = db.Column(db.Integer, db.ForeignKey('list.list_id'), nullable = False)
    list_if = db.relationship("List", backref = 'listar', lazy = True)

    def __repr__(self):
        return 'Item is:%s' % self.text

class List(db.Model):
    list_id = db.Column(db.Integer, primary_key = True, autoincrement=True)


    def __repr__(self):
        return '%s' % self.list_id
