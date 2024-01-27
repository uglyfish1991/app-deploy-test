from . import db
import datetime

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(300), unique = True)
    complete = db.Column(db.Boolean, default = False)
    timestamp = db.Column(db.DateTime(timezone=True), default = datetime.date.today)
