import pytest
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_returns_200(client):
    res = client.get('/')
    assert res.status_code == 200

def test_home_has_message(client):
    res = client.get('/')
    data = json.loads(res.data)
    assert 'message' in data
    assert 'Hello' in data['message']

def test_health_returns_healthy(client):
    res = client.get('/health')
    data = json.loads(res.data)
    assert res.status_code == 200
    assert data['status'] == 'healthy'

def test_health_shows_python(client):
    res = client.get('/health')
    data = json.loads(res.data)
    assert data['language'] == 'Python'

def test_users_returns_list(client):
    res = client.get('/api/users')
    data = json.loads(res.data)
    assert res.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 3

def test_users_have_correct_fields(client):
    res = client.get('/api/users')
    data = json.loads(res.data)
    assert 'name' in data[0]
    assert 'city' in data[0]
