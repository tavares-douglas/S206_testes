import requests
from scripts.getting_data import generate_response as gr

def test_status_and_data():
    _, response = gr()
    assert response.get('status') and len(response.get('data')) > 0

