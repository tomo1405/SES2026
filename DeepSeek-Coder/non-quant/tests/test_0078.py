import pytest
from src_0078 import task_func
from unittest.mock import patch
from io import StringIO

@pytest.fixture
def mock_data():
    return {
        'username': 'admin',
        'password': 'cGFzc3dv'  # 'password' encoded in base64
    }

def test_valid_login(mock_data):
    response = task_func(mock_data)
    assert response.status_code == 200
    assert "Login successful." in response.content.decode()

def test_invalid_login(mock_data):
    mock_data['username'] = 'invalid_user'
    response = task_func(mock_data)
    assert response.status_code == 401
    assert "Login failed." in response.content.decode()

def test_invalid_password(mock_data):
    mock_data['password'] = 'invalid_password'
    response = task_func(mock_data)
    assert response.status_code == 400
    assert "Bad Request" in response.content.decode()