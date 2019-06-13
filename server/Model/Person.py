import sys
sys.path.append("..")

from api import app, db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    hoursWorked = db.Column(db.String(50))
