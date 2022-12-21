#!/usr/bin/python3
""" Api that handles all default RestFul API actions for Items"""
from models.item import Item
from models.category import Category
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/items', methods=['GET'], strict_slashes=False)
def get_items():
    """
    Retrieves a list of all amenities
    """
    all_items= storage.all(Item).values()
    list_items= []
    for item in all_items:
        list_items.append(item.to_dict())
    return make_response(jsonify(list_items), 200)


@app_views.route('/items/<item_id>/', methods=['GET'],
                 strict_slashes=False)
def get_item(item_id):
    """ Retrieves an item """
    item = storage.get(Item, item_id)
    if not item:
        abort(404)
    return make_response(jsonify(item.to_dict()), 200)


@app_views.route('/items/<item_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_item(item_id):
    """
    Deletes an item  Object
    """
    item = storage.get(Item, item_id)
    if not item:
        abort(404)
    storage.delete(item)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/items', methods=['POST'], strict_slashes=False)
def post_item():
    """
    Creates an item
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    if 'category_id' not in request.get_json():
        abort(400, description="Missing category id")
    if 'owner_id' not in request.get_json():
        abort(400, description="Missing owner id")
    data = request.get_json()
    instance = item(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/items/<item_id>', methods=['PUT'],
                 strict_slashes=False)
def put_item(item_id):
    """
    Updates an item
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    ignore = ['id', 'created_at', 'updated_at']
    item = storage.get(Item, item_id)
    if not item:
        abort(404)
    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(Item, key, value)
    storage.save()
    return make_response(jsonify(item.to_dict()), 201)


@app_views.route('/categories/<category_id>/items', methods=['POST'], strict_slashes=False)
def post_category_item():
    """ Creates a categorys item """
    if not request.get_json():
        abort(400, description="Not a JSON")
    category = storage.get(Category, category_id)
    if 'name' not in request.get_json():
        abort(400, description="Missing item name")
    if 'owner_id' not in request.get_json():
        abort(400, description="Missing owner id")
    data = request.get_json()
    instance = Item(**data)
    instance.category_id = category.id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/categories/<category_id>/items', methods=['GET'],
                 strict_slashes=False)
def get_category_items(category_id):
    """
    Retrieves the list of all items objects
    of a specific category
    """
    category = storage.get(Category, category_id)
    if not category:
        abort(404)
    list_items = [item.to_dict() for item in category.items]
    return jsonify(list_items)

@app_views.route('/users/<user_id>/items', methods=['GET'],
                 strict_slashes=False)
def get_user_items(category_id):
    """
    Retrieves the list of all items objects
    of a specific user
    """
    user = storage.get(User, user_id)
    if not category:
        abort(404)
    list_items = [item.to_dict() for item in user.items]
    return jsonify(list_items)