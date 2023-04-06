def test_pass(app, client):
    res = client.get('/')
    assert res.status_code == 200
    assert "Register or login to get inside" in res.get_data(as_text=True)
    
def test_fail(app, client):
    res = client.get('/')
    assert res.status_code == 404
    