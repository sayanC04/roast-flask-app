from app import create_app

def test_health():
    app = create_app('testing')
    client = app.test_client()
    res = client.get('/api/v1/health')
    assert res.status_code == 200
    assert res.get_json()['status'] == 'ok'

def test_roast_api():
    app = create_app('testing')
    client = app.test_client()
    res = client.post('/api/v1/roast', json={'name': 'Sayan'})
    assert res.status_code == 200
    data = res.get_json()
    assert 'roast' in data and 'emoji' in data
