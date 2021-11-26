from scripts.deleting_data import delete_data as dd

def test_delete_data():
    raw_response = dd.delete_data()

    assert raw_response.status_code == 200