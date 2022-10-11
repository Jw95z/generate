from contextlib import nullcontext
from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import time

# Blueprints enable python code to be organized in multiple files and directories https://flask.palletsprojects.com/en/2.2.x/blueprints/
covid_api = Blueprint('covid_api', __name__,
                   url_prefix='/api/covid')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(covid_api)

def updateTime():
    global last_run  # the last_run global is preserved between calls to function
    try: last_run
    except: last_run = None
    
    # initialize last_run data
    if last_run is None:
        last_run = time.time()
        return True
    
    # calculate time since last update
    elapsed = time.time() - last_run
    if elapsed > 86400:  # update every 24 hours
        last_run = time.time()
        return True
    
    return False


def getCovidAPI():
    global covid_data  # the covid_data global is preserved between calls to function
    try: covid_data
    except: covid_data = None

    if updateTime(): # request Covid data


        url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"

        headers = {
	        "X-RapidAPI-Key": "56cf0d9c39msh90ab47fd56c02e6p1d2792jsn0f4dfaa46b90",
	        "X-RapidAPI-Host": "corona-virus-world-and-india-data.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)
        covid_data = response
    else:  # Request Covid Data
        response = covid_data

    return response


  
def getCountry(filter):
    # Request Covid Data
    response = getCovidAPI()
    # Look for Country    
    countries = response.json().get('countries_stat')
    for country in countries:  # countries is a list
        if country["country_name"].lower() == filter.lower():  # this filters for country
            return country
    
    return {"message": filter + " not found"}


 
class CovidAPI:
    """API Method to GET all Covid Data"""
    class _Read(Resource):
        def get(self):
            return getCovidAPI().json()
        
    
    class _ReadCountry(Resource):
        def get(self, filter):
            return jsonify(getCountry(filter))
        
    api.add_resource(_Read, '/')
    api.add_resource(_ReadCountry, '/<string:filter>')

      
if __name__ == "__main__": 
    server = 'https://flask.nighthawkcodingsociety.com' # run from web
    url = server + "/api/covid"
    print("World Totals")
    # This code looks for "world data"
    response = getCovidAPI()
    print("World Totals")
    world = response.json().get('world_total')  # turn response to json() so we can extract "world_total"
    for key, value in world.items():  # this finds key, value pairs in country
        print(key, value)

    print()

    # This code looks for USA in "countries_stats"
    country = getCountry("USA")
    print("USA Totals")
    for key, value in country.items():
        print(key, value)