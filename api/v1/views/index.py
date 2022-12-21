#!/usr/bin/python3
""" Index Route"""

from api.v1.views import app_views
from flask import jsonify, make_response
from models import storage
from models.category import Category
from models.city import City
from models.country import Country
from models.item import Item
from models.review import Review
from models.state import State
from models.user import User

@app_views.route('/', methods=['GET'], strict_slashes=False)
def root():
    """ API root """
    return jsonify({"APIs": ["All available API links will be listed here"]})

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ API Status """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def api_obj_stats():
    """ Return the statistics of all available objects """
    objs = {'User': User,
           'Categories': Category,
           'Countries': Country,
           'Cities': City,
           'States': State,
           'Items': Item,
           'Reviews': Review
    }
    obj_count = {k: storage.count(v) for k, v in objs.items()}
    return make_response(jsonify(obj_count), 200)
