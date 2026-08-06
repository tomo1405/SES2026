import pytest
from src_0083 import task_func

def test_login(client):
    # Test that the login page is accessible
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Username' in response.data
    assert b'Password' in response.data

    # Test that the login form is validated
    response = client.post('/login', data={'username': 'test', 'password': 'test'})
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/protected'

    # Test that the login form is not validated
    response = client.post('/login', data={'username': '', 'password': ''})
    assert response.status_code == 200
    assert b'This field is required.' in response.data

def test_logout(client):
    # Test that the logout page is accessible
    response = client.get('/logout')
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/login'

def test_protected(client):
    # Test that the protected page is accessible
    response = client.get('/protected')
    assert response.status_code == 200
    assert b'Logged in as: ' in response.data

def test_user_loader(client):
    # Test that the user loader is working correctly
    response = client.get('/protected')
    assert response.status_code == 200
    assert b'Logged in as: ' in response.data

if __name__ == '__main__':
    pytest.main()