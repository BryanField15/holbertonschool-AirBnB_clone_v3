#!/usr/bin/python3
""" returns json ok status"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def status():
    """returst status:OK in json"""
    return jsonify({"status": "OK"})
