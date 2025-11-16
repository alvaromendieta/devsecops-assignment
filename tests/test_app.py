import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_search(client):
    response = client.get('/search?q=test')
    assert response.status_code == 200

def test_greet(client):
    response = client.get('/greet?name=Alice')
    assert response.status_code == 200
