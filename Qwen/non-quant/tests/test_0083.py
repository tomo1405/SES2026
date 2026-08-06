import pytest
from src_0083 import task_func
from flask import Flask, request, session
from flask_login import current_user
from werkzeug.security import generate_password_hash

@pytest.fixture
def app():
    app = task_func('test_secret_key', 'tests/templates')
    return app

@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client

def test_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Username' in response.data
    assert b'Password' in response.data

def test_login_success(client):
    response = client.post('/login', data={'username': 'testuser', 'password': 'password'})
    assert response.status_code == 302
    assert response.location.endswith('/protected')
    assert current_user.is_authenticated
    assert current_user.id == 'testuser'

def test_login_failure(client):
    response = client.post('/login', data={'username': 'wronguser', 'password': 'wrongpassword'})
    assert response.status_code == 200
    assert b'Invalid username or password' in response.data
    assert not current_user.is_authenticated

def test_protected_route(client):
    response = client.get('/protected')
    assert response.status_code == 302
    assert response.location.endswith('/login')

    # Log in first
    client.post('/login', data={'username': 'testuser', 'password': 'password'})

    response = client.get('/protected')
    assert response.status_code == 200
    assert b'Logged in as: testuser' in response.data

def test_logout(client):
    # Log in first
    client.post('/login', data={'username': 'testuser', 'password': 'password'})

    response = client.get('/logout')
    assert response.status_code == 302
    assert response.location.endswith('/login')
    assert not current_user.is_authenticated