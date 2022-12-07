
from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import threading

global response

update_api = Blueprint('update_api', __name__,
                   url_prefix='/update')

api = Api(update_api)

def keepUpdating():
    global updateFlag

    lock.acquire()
    updateFlag += 2
    lock.release()
    threading.Timer(2.0, keepUpdating).start()

def getNewData():
    url = "https://quotes15.p.rapidapi.com/quotes/random/"
    headers = {
        "X-RapidAPI-Key": "56cf0d9c39msh90ab47fd56c02e6p1d2792jsn0f4dfaa46b90",
        "X-RapidAPI-Host": "quotes15.p.rapidapi.com"
    }

if __name__ == '__main__':
    
    lock = threading.Lock()
    updateFlag = 0
    currentFlag = updateFlag
 
    while True :
        if currentFlag == updateFlag :
            lock.acquire()
            currentFlag = updateFlag
            lock.release()
 
            response = requests.request("GET", url, headers=headers)
 
#            api.add_resource(response.json(), '/')

class Update:
    class _Read(Resource):
        def get(self):
            print("get")
            return response.json()
        
    print("add_resource")
    api.add_resource(_Read, '/')



