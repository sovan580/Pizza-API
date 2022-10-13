import pytest
from flask.testing import FlaskClient
from pizzaapi import app


@pytest.fixture
def client():
    return app.test_client()


def test_home(client: FlaskClient):
    """should be a successful GET request"""
    resp = client.get('/api/welcome')
    assert resp.status_code == 200
    assert b"Welcome to Pizza House" in resp.data

def test_home_bad_http_method(client: FlaskClient):
    """should return a Method Not Allowed response"""
    resp = client.post('/api/welcome')
    assert resp.status_code == 405