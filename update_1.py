from contextlib import nullcontext
from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import threading
import time

update1_api = Blueprint('update1_api', __name__,
                   url_prefix='/update1')

api = Api(update1_api)

def keepUpdating():
    global UpdateFlag
    url = "https://quotes15.p.rapidapi.com/quotes/random/"

    headers = {
        "X-RapidAPI-Key": "56cf0d9c39msh90ab47fd56c02e6p1d2792jsn0f4dfaa46b90",
        "X-RapidAPI-Host": "quotes15.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    UpdateFlag+=10
    threading.Timer(10.0, keepUpdating).start()
  
    return response

UpdateFlag = 0

class Quote:
        class _Read(Resource):
            def get(self):
                print("func get")
                return keepUpdating().json()
        print("api")
        api.add_resource(_Read, '/')

  
if __name__ == "__main__": 
    
    # This code looks for "world data"
#    response = keepUpdating()
    
#    threading.Timer(2.0, print(response)).start()
    
    time.sleep(1)
    # This code looks for USA in "countries_stats"
    