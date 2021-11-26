import requests

def put_data():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }
    data = {
        "id":1,
        "title":"A test title",
        "body":"A test description",
        "userId":1,
    }
    post_id = 1

    url = "https://jsonplaceholder.typicode.com/posts/"

    response = requests.put(url + str(post_id), data=data, headers=headers)
    return response, response.json(), data