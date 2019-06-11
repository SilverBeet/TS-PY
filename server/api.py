from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Phil Ka/Desktop/Coding/Python/api/Person.db'

db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    hoursWorked = db.Column(db.String(50))

@app.route('/person', methods=['GET'])
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
    
    return jsonify(output)

@app.route('/person/<id>', methods=['GET'])
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

@app.route('/person', methods=['POST'])
def create_user():
    data = request.get_json()


    newPerson = Person(first_name=data['first_name'], last_name=data['last_name'], hoursWorked=data['hoursWorked'])

    db.session.add(newPerson)
    db.session.commit()
    return jsonify({'message' : 'New user created!'})

# @app.route('/person/<id>', methods=['PUT'])
# def update_person():
#     return ''

@app.route('/person/<id>', methods=['DELETE'])
def delete_person(id):
    
    Person.query.filter_by(id=id).delete()
    
    db.session.commit()

    return jsonify({'Message':'Person with id:%s deleted' % id})

if __name__ == '__main__':
    app.run(debug=True)