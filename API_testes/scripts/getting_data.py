import requests
import json

def generate_response():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }
    url = "http://dummy.restapiexample.com/api/v1/employees"
    response = requests.get(url, headers=headers)

    return response, response.json()
    