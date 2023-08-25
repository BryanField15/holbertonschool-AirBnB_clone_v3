#!/usr/bin/python3
"""Does flask appy things"""
from flask import Flask, current_app, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
import os


app = Flask(__name__)
app.register_blueprint(app_views)

cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.teardown_appcontext
def close_storage(exception=None):
    """Closes storage on teardown"""
    storage.close()


@app.errorhandler(404)
def not_found(e):
    """returns a JSON-formatted 404 status code"""
    response = jsonify({
        'error': 'Not found',
    })
    response.status_code = 404
    return response

if __name__ == "__main__":
    HBNB_API_HOST = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    HBNB_API_PORT = os.environ.get('HBNB_API_PORT', 5000)
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
