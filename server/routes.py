# from Controller.PersonController import get_all_users

from flask import Blueprint, jsonify

from Controller.PersonController import create_user, delete_person, get_all_users, get_one_user 

routes_blueprint = Blueprint("routes", __name__)    


@routes_blueprint.route("/person", methods=["GET"])
def show():
    return get_all_users()

@routes_blueprint.route('/person/<id>', methods=['GET'])
def getOnePerson(id):
    return get_one_user(id)

@routes_blueprint.route('/person', methods=['POST'])
def createAPerson():
    return create_user()

@routes_blueprint.route('/person/<id>', methods=['DELETE'])
def deleteAPerson(id):
    return delete_person(id)
