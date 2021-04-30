import requests
from .creds import api_key
import json

def search(movie):
    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

    querystring = {"s":movie,"page":"1","r":"json"}

    headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = json.loads(response.text)
    try:
        tag = json_data['Search'][0]['imdbID']
        querystring = {"i":tag,"r":"json"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        result = json.loads(response.text)
        return result
    except KeyError:
        return ""