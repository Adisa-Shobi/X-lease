#!/usr/bin/python3
""" Flask Base Application """

from flask import Flask, jsonify, make_response
from flask_cors import CORS
from api.v1.views import app_views
from models import storage
from os import environ

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """
    404 Error
    description: A resource was not found
    """
    return jsonify(error=str(error)), 404

if __name__ == "__main__":
    host = environ.get('API_HOST')
    port = environ.get('API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5001'
    app.run(host=host, port=port, threaded=True)
