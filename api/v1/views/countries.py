#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Country """

from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models.country import Country

@app_views.route('/countries', methods=['GET'], strict_slashes=False)
def get_countries():
    """
    Retrieves the list of all Country objects
    """
    all_country = storage.all(Country).values()
    list_country = [country.to_dict() for country in all_country]
    return jsonify(list_country)

@app_views.route('/countries/<country_id>', methods=['GET'], strict_slashes=False)
def get_country(country_id):
    """ Retrieves a specific Country """
    country = storage.get(Country, country_id)
    if not country:
        abort(404)
    return jsonify(country.to_dict())

@app_views.route('/countries/<country_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_country(country_id):
    """ Deletes a Country Object """
    country = storage.get(Country, country_id)
    if not country:
        abort(404)
    storage.delete(country)
    storage.save()
    return make_response(jsonify({}), 200)

@app_views.route('/countries', methods=['POST'], strict_slashes=False)
def post_country():
    """ Create a Country object """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing country name")
    data = request.get_json()
    instance = Country(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/countries/<country_id>', methods=['PUT'], strict_slashes=False)
def put_country(country_id):
    """ Updates a Country """
    country = storage.get(Country, country_id)
    if not country:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    read_only = ['id', 'created_at', 'updated_at']
    data = request.get_json()
    for key, value in data.items():
        if key not in read_only:
            setattr(country, key, value)
    storage.save()
    return make_response(jsonify(country.to_dict()), 200)