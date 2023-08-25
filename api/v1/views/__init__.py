#!/usr/bin/python3
"""Instanciates app_view blueprint and imports all indexes"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.places import *
from api.v1.views.users import *
<<<<<<< HEAD
#from api.v1.views.places import *
from api.v1.views.reviews import *
=======
#from api.v1.views.reviews import *
>>>>>>> 8ce83c634ec61544609f59c7b6fb7f844eb3ddac
