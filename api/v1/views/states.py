#!/usr/bin/python3
""" objects that handle all default RestFul API actions for States """

from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models.country import Country
from models.state import State

@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """
    Retrieves the list of all State objects
    """
    all_states = storage.all(State).values()
    list_states = [state.to_dict() for state in all_states]
    return jsonify(list_states)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """ Retrieves a specific State """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    state_cities = [i.to_dict() for i in state.cities]
    state_obj = state.to_dict()
    state_obj["cities"] = state_cities
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """ Deletes a State Object """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    storage.delete(state)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post_state():
    """ Creates a State """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing state name")
    if 'country_id' not in request.get_json():
        abort(400, description="Missing country id")
    data = request.get_json()
    instance = State(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/countries/<country_id>/states', methods=['POST'], strict_slashes=False)
def post_country_state():
    """ Creates a countrys State """
    if not request.get_json():
        abort(400, description="Not a JSON")
    country = storage.get(Country, country_id)
    if 'name' not in request.get_json():
        abort(400, description="Missing state name")
    data = request.get_json()
    instance = State(**data)
    instance.country_id = country.id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def put_state(state_id):
    """ Updates a State """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    read_only = ['id', 'created_at', 'updated_at']
    data = request.get_json()
    for key, value in data.items():
        if key not in read_only:
            setattr(state, key, value)
    storage.save()
    return make_response(jsonify(state.to_dict()), 200)


@app_views.route('/countries/<country_id>/states', methods=['GET'],
                 strict_slashes=False)
def get_country_states(country_id):
    """
    Retrieves the list of all states objects
    of a specific country
    """
    list_states = []
    country = storage.get(Country, country_id)
    if not country:
        abort(404)
    for state in country.states:
        list_states.append(state.to_dict())
    return jsonify(list_states)
