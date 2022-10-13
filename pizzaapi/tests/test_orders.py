import pytest
from flask.testing import FlaskClient
from pizzaapi import app


@pytest.fixture
def client():
    return app.test_client()

def test_getorders_bad_http_method(client: FlaskClient):
    """should return a Method Not Allowed response"""
    resp = client.post('/api/getorders')
    assert resp.status_code == 405

def test_order_bad_http_method(client: FlaskClient):
    """should return a Method Not Allowed response"""
    resp = client.get('/api/order')
    assert resp.status_code == 405

def test_single_order_bad_http_method(client: FlaskClient):
    """should return a Wrong Object Id Error"""
    resp = client.get('/api/getorders/2323')
    assert resp.status_code == 400