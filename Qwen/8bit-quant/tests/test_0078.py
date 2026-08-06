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
    assert response.content.decode() == 'Login successful.'

def test_task_func_invalid_username():
    data = {
        'username': 'user',
        'password': base64.b64encode(b'password').decode()
    }
    response = task_func(data)
    assert isinstance(response, HttpResponse)
    assert response.content.decode() == 'Login failed.'
    assert response.status_code == 401

def test_task_func_invalid_password():
    data = {
        'username': 'admin',
        'password': base64.b64encode(b'wrongpassword').decode()
    }
    response = task_func(data)
    assert isinstance(response, HttpResponse)
    assert response.content.decode() == 'Login failed.'
    assert response.status_code == 401

def test_task_func_missing_username():
    data = {
        'password': base64.b64encode(b'password').decode()
    }
    response = task_func(data)
    assert isinstance(response, HttpResponseBadRequest)
    assert response.content.decode() == 'Bad Request'

def test_task_func_missing_password():
    data = {
        'username': 'admin'
    }
    response = task_func(data)
    assert isinstance(response, HttpResponseBadRequest)
    assert response.content.decode() == 'Bad Request'

def test_task_func_invalid_base64_password():
    data = {
        'username': 'admin',
        'password': 'invalid_base64'
    }
    response = task_func(data)
    assert isinstance(response, HttpResponseBadRequest)
    assert response.content.decode() == 'Bad Request'