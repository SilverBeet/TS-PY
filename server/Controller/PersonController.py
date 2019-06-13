import sys
sys.path.append("..")

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Phil Ka/Desktop/Coding/stack/TS-PY/server/database/Person.db'

db = SQLAlchemy(app)

# from Model.Person import Person, db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    hoursWorked = db.Column(db.String(50))

# GET ALL PERSONS
def get_all_users():
    persons = Person.query.all()
    output = []
    for person in persons:
        person_data = {}
        person_data['id'] = person.id
        person_data['first_name'] = person.first_name
        person_data['last_name'] = person.last_name
        person_data['hoursWorked'] = person.hoursWorked
        output.append(person_data)
    return output

# GET ONE PERSONS
def get_one_user(id):
    person = Person.query.filter_by(id=id).first()
    if not person:
        return jsonify({'Message':'Person with id:%s does not exist' % id})
    person_data = {}
    person_data['id'] = person.id
    person_data['first_name'] = person.first_name
    person_data['last_name'] = person.last_name
    person_data['hoursWorked'] = person.hoursWorked
    return jsonify(person_data)

# CREATE ONE PERSONS
def create_user():
    data = request.get_json()
    newPerson = Person(first_name=data['first_name'], last_name=data['last_name'], hoursWorked=data['hoursWorked'])
    db.session.add(newPerson)
    db.session.commit()
    return jsonify({'message' : 'New user created!'})

# UPDATE ONE PERSON
# @app.route('/person/<id>', methods=['PUT'])
# def update_person(id):
#     return ''

# DELETE ONE PERSON
def delete_person(id):
    Person.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({'Message':'Person with id:%s deleted' % id})