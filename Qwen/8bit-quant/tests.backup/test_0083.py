import pytest
from src_0083 import task_func
from flask import Flask, session
from flask_login import login_user, logout_user, current_user
from werkzeug.security import generate_password_hash

@pytest.fixture
def app():
    app = task_func('secret_key', 'templates')
    return app

@pytest.fixture
def client(app):
    with app.test_client() as client:
        with app.app_context():
            yield client

@pytest.fixture
def user():
    return {'username': 'testuser', 'password': 'password'}

def test_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Username' in response.data
    assert b'Password' in response.data

def test_successful_login(client, user):
    response = client.post('/login', data=user, follow_redirects=True)
    assert response.status_code == 200
    assert b'Logged in as: testuser' in response.data
    assert current_user.is_authenticated

def test_failed_login(client, user):
    user['password'] = 'wrongpassword'
    response = client.post('/login', data=user, follow_redirects=True)
    assert response.status_code == 200
    assert b'Username' in response.data
    assert b'Password' in response.data
    assert not current_user.is_authenticated

def test_logout(client, user):
    client.post('/login', data=user, follow_redirects=True)
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Username' in response.data
    assert b'Password' in response.data
    assert not current_user.is_authenticated

def test_protected_page_without_login(client):
    response = client.get('/protected', follow_redirects=True)
    assert response.status_code == 200
    assert b'Username' in response.data
    assert b'Password' in response.data
    assert not current_user.is_authenticated

def test_protected_page_with_login(client, user):
    client.post('/login', data=user, follow_redirects=True)
    response = client.get('/protected')
    assert response.status_code == 200
    assert b'Logged in as: testuser' in response.data
    assert current_user.is_authenticated