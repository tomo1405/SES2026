python
import hashlib
import base64
import binascii
from django.http import HttpResponseBadRequest, HttpResponse
from src_0078 import task_func

def test_task_func():
    # Test case 1: Valid input data
    data = {
        'username': 'admin',
        'password': base64.b64encode('password'.encode()).decode()
    }
    response = task_func(data)
    assert response.status_code == 200
    assert response.content == b'Login successful.'

    # Test case 2: Invalid input data (missing username)
    data = {
        'password': base64.b64encode('password'.encode()).decode()
    }
    response = task_func(data)
    assert response.status_code == 400
    assert response.content == b'Bad Request'

    # Test case 3: Invalid input data (invalid base64 encoding)
    data = {
        'username': 'admin',
        'password': 'invalid_base64_encoding'
    }
    response = task_func(data)
    assert response.status_code == 400
    assert response.content == b'Bad Request'

    # Test case 4: Invalid input data (invalid UTF-8 encoding)
    data = {
        'username': 'admin',
        'password': base64.b64encode('password'.encode('utf-16')).decode()
    }
    response = task_func(data)
    assert response.status_code == 400
    assert response.content == b'Bad Request'

    # Test case 5: Invalid input data (invalid SHA256 hash)
    data = {
        'username': 'admin',
        'password': base64.b64encode('invalid_password'.encode()).decode()
    }
    response = task_func(data)
    assert response.status_code == 401
    assert response.content == b'Login failed.'