#!/usr/bin/python3
"""View for Place objects that handles all default RESTFul API actions"""
from flask import Flask, jsonify, abort, request
from models.place import Place
from models.city import City
from models.user import User
from api.v1.views import app_views
from models import storage


@app_views.route('/cities/<city_id>/places', methods=['GET'], strict_slashes=False)
def get_places_by_city(city_id):
    """Retrieves the list of all Place objects in a city"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    return jsonify([place.to_dict() for place in city.places])


@app_views.route('/places/<place_id>', methods=['GET'],
                 strict_slashes=False)
def get_place(place_id):
    """Retrieves a Place object"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_place(place_id):
    """Deletes a Place object"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    storage.delete(place)
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places', methods=['POST'], strict_slashes=False)
def create_place_by_city(city_id):
    """Creates a Place"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    if 'name' not in data:
        return jsonify({"error": "Missing name"}), 400
    new_place = Place(**data)
    new_place.city_id = city_id
    new_place.save()
    return jsonify(new_place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'],
                 strict_slashes=False)
def update_place(place_id):
    """Updates a Place object"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    for key, value in data.items():
        if key not in ['id',
                       'user_id',
                       'city_id',
                       'created_at',
                       'updated_at']:
            setattr(place, key, value)
    place.save()
    return jsonify(place.to_dict()), 200
