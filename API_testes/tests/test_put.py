from scripts.putting_data import put_data as pd

def test_put_new_data():
    raw_response, _, data = pd.put_data()
    if raw_response.status_code == 200:
        assert raw_response == data
    else:
        assert False