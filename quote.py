import requests
import threading
def keepUpdating():
    url = "https://famous-quotes4.p.rapidapi.com/random"

    querystring = {"category":"all","count":"1"}

    headers = {
        "X-RapidAPI-Key": "56cf0d9c39msh90ab47fd56c02e6p1d2792jsn0f4dfaa46b90",
        "X-RapidAPI-Host": "famous-quotes4.p.rapidapi.com"
    }
            
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    threading.Timer(10.0, keepUpdating).start()
threading.Timer(10.0, keepUpdating).start()