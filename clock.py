from contextlib import nullcontext
from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource 
import datetime
from threading import Timer

clocks = Blueprint('clocks',__name__, url_prefix='/clocks')
global x
api = Api(clocks)


