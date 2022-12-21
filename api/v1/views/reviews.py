#!/usr/bin/python3
'''
Endpoint definitions for retrieving Reviews
'''

from models import storage
from models.review import Review
from models.user import User
from models.item import Item
from api.v1.views import app_views
from flask import make_response, abort, request, jsonify


@app_views.route('/reviews', methods=['GET', 'POST'], strict_slashes=False)
def get_reviews():
    '''
    Endpoint for retrieving/creating review data
    '''
    if request.method == "POST":
        data = request.get_json()
        if not data:
            abort(404, description='Invalid JSON')
        data_keys = data.keys()
        compulsory_data = ['item_id', 'user_id', 'text']
        if not set(compulsory_data).issubset(set(data_keys)):
            abort(404, description='Insufficient data supplied')
        new_review = Review(**data)
        new_review.save()
        return make_response(jsonify(new_review.to_dict()), 201)
    else:
        reviews = storage.all(Review)
        if not reviews:
            abort(404, description='No reviews found')
        reviews_dict = list(map(lambda x: x.to_dict(), reviews.values()))
        return jsonify(reviews_dict)


@app_views.route('/reviews/<review_id>', methods=['GET', 'PUT', 'DELETE'],
                 strict_slashes=False)
def get_review(review_id):
    '''Endpoint for retrieving, updating and deleting data
    '''
    review = storage.get(Review, review_id)
    if not review:
        abort(404, description='review_id does not exist')

    if request.method == 'PUT':
        read_only = ['id', 'created_at', 'updated_at']
        data = request.get_json()
        if not data:
            abort(404, description='Invalid JSON')
        for info in data:
            if info not in read_only:
                setattr(review, info, data[info])
        review.save()
        return jsonify(review.to_dict())
    elif request.method == 'DELETE':
        storage.delete(review)
        storage.save()
        return jsonify({})
    else:
        return jsonify(review.to_dict())


@app_views.route('/users/<user_id>/reviews', methods=['POST', 'GET'],
                 strict_slashes=False)
def get_user_reviews(user_id):
    '''Retrieves all reviews made by specified user
    '''
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            abort(404, description='Invalid JSON')
        data['user_id'] = user_id
        data_keys = data.keys()
        compulsory_data = ['item_id', 'user_id', 'text']
        if not set(compulsory_data).issubset(set(data_keys)):
            abort(404, description='Insufficient data supplied')
        new_review = Review(**data)
        new_review.save()
        return make_response(jsonify(new_review.to_dict()), 201)
    else:
        user = storage.get(User, user_id)
        if not user:
            abort(404, description='user_id does not exist')
        reviews = user.reviews
        reviews_dict = list(map(lambda x: x.to_dict(), reviews))
        return jsonify(reviews_dict)


@app_views.route('/users/<user_id>/reviews/<review_id>', methods=['GET'],
                 strict_slashes=False)
def get_user_review(user_id, review_id):
    '''Retrieves specified review made by specified user
    '''
    user = storage.get(User, user_id)
    if not user:
        abort(404, description='user_id does not exist')
    reviews = user.reviews
    for review in reviews:
        if review.id == review_id:
            matched_review = review
            break
    return jsonify(reviews_dict.to_dict())


@app_views.route('/items/<item_id>/reviews', methods=['POST', 'GET'],
                 strict_slashes=False)
def get_item_reviews(item_id):
    '''Retrieves all reviews made by specified item
    '''
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            abort(404, description='Invalid JSON')
        data['item_id'] = item_id
        data_keys = data.keys()
        compulsory_data = ['item_id', 'user_id', 'text']
        if not set(compulsory_data).issubset(set(data_keys)):
            abort(404, description='Insufficient data supplied')
        new_review = Review(**data)
        new_review.save()
        return make_response(jsonify(new_review.to_dict()), 201)
    else:
        item = storage.get(Item, item_id)
        if not item:
            abort(404, description='item_id does not exist')
        reviews = item.reviews
        reviews_dict = list(map(lambda x: x.to_dict(), reviews))
        return jsonify(reviews_dict)


@app_views.route('/items/<item_id>/reviews/<review_id>', methods=['GET'],
                 strict_slashes=False)
def get_item_review(item_id, review_id):
    '''Retrieves specified review made by specified item
    '''
    item = storage.get(Item, item_id)
    if not item:
        abort(404, description='item_id does not exist')
    reviews = item.reviews
    for review in reviews:
        if review.id == review_id:
            matched_review = review
            break
    return jsonify(reviews_dict.to_dict())
