print "starting"
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from factory import creat_app
#db.init_app(app)

app = creat_app()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#db = SQLAlchemy(app)
db.init_app(app)
