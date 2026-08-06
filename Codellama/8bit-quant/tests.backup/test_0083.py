import pytest
from src_0083 import task_func

def test_login_form_valid_data():
    app = task_func('secret_key', 'template_folder')
    with app.test_client() as c:
        response = c.post('/login', data={'username': 'test_user', 'password': 'test_password'})
        assert response.status_code == 302
        assert response.headers['Location'] == 'http://localhost/protected'

def test_login_form_invalid_data():
    app = task_func('secret_key', 'template_folder')
    with app.test_client() as c:
        response = c.post('/login', data={'username': 'test_user', 'password': 'invalid_password'})
        assert response.status_code == 200
        assert b'Invalid username or password' in response.data

def test_logout():
    app = task_func('secret_key', 'template_folder')
    with app.test_client() as c:
        response = c.get('/logout')
        assert response.status_code == 302
        assert response.headers['Location'] == 'http://localhost/login'

def test_protected():
    app = task_func('secret_key', 'template_folder')
    with app.test_client() as c:
        response = c.get('/protected')
        assert response.status_code == 200
        assert b'Logged in as: test_user' in response.data