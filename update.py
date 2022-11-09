import threading
import requests
from flask import Blueprint, jsonify  
from flask_restful import Api, Resource
update = Blueprint('update', __name__,
                   url_prefix='/update')


api = Api(update)

def keepUpdating():
    url = "https://motivational-quotes1.p.rapidapi.com/motivation"

    payload = {
	    "key1": "value",
	    "key2": "value"
    }
    headers = {
	    "content-type": "application/json",
	    "X-RapidAPI-Key": "56cf0d9c39msh90ab47fd56c02e6p1d2792jsn0f4dfaa46b90",
	    "X-RapidAPI-Host": "motivational-quotes1.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.text)
    threading.Timer(2.0, keepUpdating).start()
threading.Timer(2.0, keepUpdating).start()