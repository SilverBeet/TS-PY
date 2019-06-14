import wsgiserver

from flask_cors import CORS
from Model.Person import app
from routes import routes_blueprint

CORS(app)

app.register_blueprint(routes_blueprint)

server = wsgiserver.WSGIServer(app, host='127.0.0.1', port=5000)
server.start()

# if __name__ == '__main__':
#     app.run(debug=True)
