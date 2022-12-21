#!/usr/bin/python3
'''
Endpoints defined fpr all item retrievals
'''
from api.v1.views import app_views
from models import storage
from flask import abort, jsonify, make_response, request
from models.item import Item
from models.category import Category
from models.user import User


@app_views.route('/items', methods=['GET', 'POST'], strict_slashes=False)
def get_items():
    '''
    Retrieves all items
    '''
    if request.method == 'POST':
        data = requests.get_json()
        if not data:
            abort(404, description='Invalid JSON')
        data_keys = data.keys()
        compulsory_data = ['owner_id', 'name', 'price', 'price_per_day',
                           'description', 'category_id', 'owner_id']
        if not set(compulsory_data).issubset(set(data_keys)):
            abort(404, description='insufficient data supplied')
        new_item = Item(**data)
        new_item.save()
        return make_response(jsonify(new_item.to_dict()), 201)
    else:
        items = storage.all(Item)
        if not items:
            abort(404, description='there are currently no available items')
        item_list = list(map(lambda x: x.to_dict(), items.values()))
        return jsonify(item_list)


@app_views.route('items/<item_id>', methods=['GET', 'PUT', 'DELETE'],
                 strict_slashes=False)
def get_item(item_id=None):
    '''
    Retrieves item specified by item_id
    '''
    item = storage.get(Item, item_id)
    if not item:
        abort(404, description='item_id does not exist')

    if request.method == 'PUT':
        read_only = ['id', 'created_at', 'updated_at']
        data = request.get_json()
        if not data:
            abort(404, description='Invalid JSON')
        for info in data:
            if info not in read_only:
                setattr(item, info, data[info])
                print(data[info])
        item.save()
        return make_response(jsonify(item.to_dict()), 200)
    elif request.method == 'DELETE':
        storage.delete(item)
        storage.save()
        return make_response(jsonify({}), 201)
    else:
        return jsonify(item.to_dict())


@app_views.route('/categories/<category_id>/items',
                 methods=['GET', 'POST'],
                 strict_slashes=False)
def get_items_by_category(category_id=None):
    '''
    Retrieves all items under specified category
    '''
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            abort(404, description='Invalid JSON')
        data['category_id'] = category_id
        data_keys = data.keys()
        compulsory_data = ['owner_id', 'name', 'price', 'price_per_day',
                           'description', 'category_id', 'owner_id']
        if not set(compulsory_data).issubset(set(data_keys)):
            abort(404, description='insufficient data supplied')
        new_item = Item(**data)
        new_item.save()
        return make_response(jsonify(new_item.to_dict()), 201)
    else:
        category = storage.get(Category, category_id)
        if not category:
            abort(404, description='category_id does not exist')
        category_items = category.items
        items_dict = list(map(lambda x: x.to_dict(), category_items))
        return jsonify(items_dict)


@app_views.route('/categories/<category_id>/items/<item_id>',
                 methods=['GET'],
                 strict_slashes=False)
def get_item_by_category(category_id=None, item_id=None):
    '''
    Retrieves specified item under specified category
    '''
    category = storage.get(Category, category_id)
    if not category:
        abort(404,
              description='category_id does not exist')
    category_items = category.items
    for item in category_items:
        if item.id == item_id:
            matched_item = item
    if not matched_item:
        abort(404,
              description='item_id does not exist under specified category')
    return jsonify(matched_item.to_dict())


@app_views.route('/users/<user_id>/items',
                 methods=['GET', 'POST'],
                 strict_slashes=False)
def get_user_items(user_id):
    '''
    Retrieves items for specified user_id
    '''
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            abort(404, description='Invalid JSON')
        data['user_id'] = user_id
        data_keys = data.keys()
        compulsory_data = ['owner_id', 'name', 'price', 'price_per_day',
                           'description', 'category_id', 'owner_id']
        if not set(compulsory_data).issubset(set(data_keys)):
            abort(404, description='insufficient data supplied')
        new_item = Item(**data)
        new_item.save()
        return make_response(jsonify(new_item.to_dict()), 201)
    else:
        user = storage.get(User, user_id)
        if not user:
            abort(404, description='user_id does not exist')
        user_items = user.items
        if not user_items:
            abort(404, 'Specified user owns no items')
        items_dict = list(map(lambda x: x.to_dict(), user_items))
        return jsonify(items_dict)


@app_views.route('/users/<user_id>/items/<item_id>',
                 methods=['GET'],
                 strict_slashes=False)
def get_user_item(user_id, item_id):
    '''
    Retrieves specified item for specified user_id
    '''
    user = storage.get(User, user_id)
    if not user:
        abort(404, description='user_id does not exist')
    user_items = user.items
    if not user_items:
        abort(404, 'Specified user owns no items')
    for item in user_items:
        if item.id == item_id:
            matched_item = item
            break
    if not matched_item:
        abort(404, description='item_id does not exist')
    return jsonify(matched_item.to_dict())
