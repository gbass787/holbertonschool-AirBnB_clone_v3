#!/usr/bin/python3
"""returns status of an API"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv
from flask import jsonify
from werkzeug.exceptions import HTTPException


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    storage.close()


@app.errorhandler(HTTPException)
def handle_exception(error):
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True, debug=True)
