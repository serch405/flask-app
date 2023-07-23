def test_home_page(app, client):
    res = client.get('/')
    assert res.status_code == 200
    assert "Register or login to get inside" in res.get_data(as_text=True)
    
def test_faq_page(app, client):
    res = client.get('/faq')
    assert res.status_code == 200

def test_users_endpoint(app, client):
    res = client.get('/api/users')
    assert res.status_code == 200
    