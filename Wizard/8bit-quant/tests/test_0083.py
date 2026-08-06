python
import pytest
from src_0083 import task_func

def test_task_func():
    app = task_func('secret_key', 'templates')
    with app.test_client() as client:
        response = client.get('/login')
        assert response.status_code == 200
        assert b'Log In' in response.data
        assert b'Username' in response.data
        assert b'Password' in response.data
        assert b'Log In' in response.data

        response = client.post('/login', data={'username': 'user', 'password': 'password'})
        assert response.headers['Location'] == 'http://localhost/protected'

        response = client.get('/protected')
        assert response.data == b'Logged in as: user'

        response = client.get('/logout')
        assert response.headers['Location'] == 'http://localhost/login'