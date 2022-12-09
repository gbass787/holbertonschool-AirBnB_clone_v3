#!/usr/bin/python3
''' module that have the get status '''

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def get_status():
    ''' route status test that return a JSON query '''
    dict = {'status': 'OK'}
    return jsonify(dict)
