from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from routes import routes_blueprint

app = Flask(__name__)
CORS(app)

app.register_blueprint(routes_blueprint)
app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Phil Ka/Desktop/Coding/stack/TS-PY/server/database/Person.db'

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)
