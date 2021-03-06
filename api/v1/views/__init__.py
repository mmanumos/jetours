""" Init views """
from flask import Blueprint
# The blueprint is recorded in order to able use the views
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

if app_views is not None:
    from api.v1.views.index import *
