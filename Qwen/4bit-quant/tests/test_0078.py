import base64

from django.http import HttpResponse, HttpResponseBadRequest
from src_0078 import task_func


def test_task_func_valid_credentials():
    data = {
        'username': 'admin',
        'password': base64.b64encode(b'password').decode()
    }
    response = task_func(data)
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.content == b'Login successful.'

def test_task_func_invalid_credentials():
    data = {
        'username': 'admin',
        'password': base64.b64encode(b'wrongpassword').decode()
    }
    response = task_func(data)
    assert isinstance(response, HttpResponse)
    assert response.status_code == 401
    assert response.content == b'Login failed.'

def test_task_func_missing_username():
    data = {
        'password': base64.b64encode(b'password').decode()
    }
    response = task_func(data)
    assert isinstance(response, HttpResponseBadRequest)
    assert response.status_code == 400
    assert response.content == b'Bad Request'

def test_task_func_missing_password():
    data = {
        'username': 'admin'
    }
    response = task_func(data)
    assert isinstance(response, HttpResponseBadRequest)
    assert response.status_code == 400
    assert response.content == b'Bad Request'

def test_task_func_invalid_base64_password():
    data = {
        'username': 'admin',
        'password': 'invalid_base64_string'
    }
    response = task_func(data)
    assert isinstance(response, HttpResponseBadRequest)
    assert response.status_code == 400
    assert response.content == b'Bad Request'

def test_task_func_unicode_decode_error():
    data = {
        'username': 'admin',
        'password': base64.b64encode(b'\xff').decode()
    }
    response = task_func(data)
    assert isinstance(response, HttpResponseBadRequest)
    assert response.status_code == 400
    assert response.content == b'Bad Request'