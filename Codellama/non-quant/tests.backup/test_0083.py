import pytest
from src_0083 import task_func

def test_login_form():
    app = task_func('secret_key', 'template_folder')
    client = app.test_client()
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Username' in response.data
    assert b'Password' in response.data
    assert b'Log In' in response.data

def test_login_form_submit():
    app = task_func('secret_key', 'template_folder')
    client = app.test_client()
    response = client.post('/login', data={'username': 'test_user', 'password': 'test_password'})
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/protected'

def test_logout():
    app = task_func('secret_key', 'template_folder')
    client = app.test_client()
    response = client.get('/logout')
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/login'

def test_protected():
    app = task_func('secret_key', 'template_folder')
    client = app.test_client()
    response = client.get('/protected')
    assert response.status_code == 200
    assert b'Logged in as: test_user' in response.data

def test_user_loader():
    app = task_func('secret_key', 'template_folder')
    client = app.test_client()
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Username' in response.data
    assert b'Password' in response.data
    assert b'Log In' in response.data

if __name__ == '__main__':
    pytest.main()