#!/usr/bin/python3
"""Does flask appy things"""
from flask import Flask, current_app
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def close_storage(exception=None):
    """Closes storage on teardown"""
    storage.close()

if __name__ == "__main__":
    HBNB_API_HOST = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    HBNB_API_PORT = os.environ.get('HBNB_API_PORT', 5000)
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
