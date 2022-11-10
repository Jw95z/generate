import threading
import requests
from flask import Blueprint, jsonify  
from flask_restful import Api, Resource
update = Blueprint('update', __name__,
                   url_prefix='/update')

api = Api(update)

def keepUpdating():
    global response
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

    response = requests.request("GET", url, json=payload, headers=headers)
    print(response)
    threading.Timer(2.0, keepUpdating).start()




"""Defines API Resources 
  URLs are defined with api.add_resource
"""   



"""Main or Tester Condition 
  This code only runs when this file is played directly
"""        
if __name__ == "__main__": 
    
    # This code looks for "world data"
    threading.Timer(2.0, keepUpdating).start()
    
     # turn response to json() so we can extract "world_total"

    # This code looks for USA in "countries_stats"
