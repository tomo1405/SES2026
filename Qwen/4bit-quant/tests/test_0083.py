import pytest
from src_0083 import task_func
from flask import Flask, request
from flask_login import current_user
from werkzeug.security import generate_password_hash

@pytest.fixture
def app():
    app = task_func('test_secret_key', 'templates')
    return app

@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client

@pytest.fixture
def user():
    return User('test_user', 'test_password')

class User(UserMixin):
    def __init__(self, username, password):
        self.id = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

def test_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Username' in response.data
    assert b'Password' in response.data

def test_login_with_valid_credentials(client, user):
    response = client.post('/login', data={
        'username': user.id,
        'password': 'test_password'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Logged in as: test_user' in response.data
    assert current_user.is_authenticated

def test_login_with_invalid_credentials(client, user):
    response = client.post('/login', data={
        'username': user.id,
        'password': 'wrong_password'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Username' in response.data
    assert b'Password' in response.data
    assert not current_user.is_authenticated

def test_logout(client, user):
    client.post('/login', data={
        'username': user.id,
        'password': 'test_password'
    }, follow_redirects=True)
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Username' in response.data
    assert b'Password' in response.data
    assert not current_user.is_authenticated

def test_protected_route(client, user):
    client.post('/login', data={
        'username': user.id,
        'password': 'test_password'
    }, follow_redirects=True)
    response = client.get('/protected')
    assert response.status_code == 200
    assert b'Logged in as: test_user' in response.data
    assert current_user.is_authenticated

def test_protected_route_without_login(client):
    response = client.get('/protected', follow_redirects=True)
    assert response.status_code == 200
    assert b'Username' in response.data
    assert b'Password' in response.data
    assert not current_user.is_authenticated