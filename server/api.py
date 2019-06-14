from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from Model.Person import app
from routes import routes_blueprint

CORS(app)

app.register_blueprint(routes_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
