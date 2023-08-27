#!/usr/bin/python3
"""View for Review objects that handles all default RESTFul API actions"""
from flask import Flask, jsonify, abort, request
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from api.v1.views import app_views
from models import storage


@app_views.route('/places/<place_id>/reviews',
                 methods=['GET'],
                 strict_slashes=False)
def get_reviews(place_id):
    """Retrieves the list of all Review objects of a Place"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    return jsonify([review.to_dict() for review in place.reviews])


@app_views.route('/reviews/<review_id>',
                 methods=['GET'],
                 strict_slashes=False)
def get_review(review_id):
    """Retrieves a Review object"""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>',
                 methods=['DELETE'],
                 strict_slashes=False)
def delete_review(review_id):
    """Deletes a Review object"""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    review.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/places/<place_id>/reviews',
                 methods=['POST'],
                 strict_slashes=False)
def post_review(place_id):
    """Creates a Review"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    data = request.get_json()
    if 'user_id' not in data:
        abort(400, "Missing user_id")
    user = storage.get(User, data['user_id'])
    if not user:
        abort(404)
    if 'text' not in data.keys():
        abort(400, "Missing text")
    review = User.create(**data)
    storage.save()
    return jsonify(review.to_dict()), 201


@app_views.route('/reviews/<review_id>',
                 methods=['PUT'],
                 strict_slashes=False)
def put_review(review_id):
    """Updates a Review object"""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in [
            'id',
            'user_id',
            'place_id',
            'created_at',
            'updated_at']:
            setattr(review, key, value)
    storage.save()
    return jsonify(review.to_dict()), 200
