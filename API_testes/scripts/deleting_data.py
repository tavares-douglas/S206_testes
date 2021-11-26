import requests

def delete_data():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }
    post_id = 1
    url = "https://jsonplaceholder.typicode.com/posts/"
    response = requests.delete(url + str(post_id), headers=headers)
    
    return response, response.json()