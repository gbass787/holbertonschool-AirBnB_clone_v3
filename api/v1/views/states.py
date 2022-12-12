#!/usr/bin/python3
''' Module that handles all default RESTFul API '''

from flask import jsonify, abort, request, Response
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route('/states', methods=['GET', 'POST'], strict_slashes=False)
def get_states():
    """ focus on all the state object """

    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return Response("Not a JSON", 400)
        if 'name' not in data:
            return Response("Missing name", 400)
        state = State(name=data.get('name'))
        state.save()
        return jsonify(state.to_dict()), 201

    all_states = storage.all('State')
    states = []

    for state in all_states.values():
        states.append(state.to_dict())
    return jsonify(states)


@app_views.route('/states/<state_id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def get_state(state_id=None):
    """ focus on a single state object """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    if request.method == 'DELETE':
        storage.delete(state)
        storage.save()
        return jsonify({}), 200

    if request.method == 'PUT':
        data = request.get_json()
        if not data:
            return Response("Not a JSON", 400)
        data['id'] = state.id
        data['created_at'] = state.created_at
        state.__init__(**data)
        state.save()
        return jsonify(state.to_dict()), 200

    return jsonify(state.to_dict())
