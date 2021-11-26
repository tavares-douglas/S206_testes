import requests

def insert_data():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }
    url = "http://dummy.restapiexample.com/api/v1/create"
    new_employee = {"name": "Testerson", "salary": 5000, "age":32}
    response = requests.post(url, headers=headers, data=new_employee)

    return response, response.json()