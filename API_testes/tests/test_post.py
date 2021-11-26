import requests
from scripts.inserting_data import insert_data as ind

def test_status_and_data():
    raw_response, response = ind.insert_data()
    if raw_response.status_code == 200:
        status = response.get('status')
        employee_response = response.get('data')

        assert status == "success" and employee_response.get("id") is not None
    else:
        assert False