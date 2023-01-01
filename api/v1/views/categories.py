#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Category """

from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models.category import Category

@app_views.route('/categories', methods=['GET'], strict_slashes=False)
def get_categoties():
    """
    Retrieves the list of all Category objects
    """
    all_categories = storage.all(Category).values()
    list_categories = [category.to_dict() for category in all_categories]
    return jsonify(list_categories)

@app_views.route('/categories/<category_id>', methods=['GET'], strict_slashes=False)
def get_category(category_id):
    """ Retrieves a specific Category """
    category = storage.get(Category, category_id)
    if not category:
        abort(404)
    cat_item = [i.to_dict() for i in category.items]
    cat_obj = category.to_dict()
    cat_obj["items"] = cat_item
    return jsonify(cat_obj)

@app_views.route('/categories/<category_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_category(category_id):
    """ Deletes a Category Object """
    category = storage.get(Category, category_id)
    if not category:
        abort(404)
    storage.delete(category)
    storage.save()
    return make_response(jsonify({}), 200)

@app_views.route('/categories', methods=['POST'], strict_slashes=False)
def post_category():
    """ Create a Category object """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing category name")
    data = request.get_json()
    instance = Category(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/categories/<category_id>', methods=['PUT'], strict_slashes=False)
def put_category(category_id):
    """ Updates a Category """
    category = storage.get(Category, category_id)
    if not category:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    read_only = ['id', 'created_at', 'updated_at']
    data = request.get_json()
    for key, value in data.items():
        if key not in read_only:
            setattr(category, key, value)
    storage.save()
    return make_response(jsonify(category.to_dict()), 200)
