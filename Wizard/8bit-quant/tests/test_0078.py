python
import hashlib
import base64
import binascii
from django.http import HttpResponseBadRequest, HttpResponse
import pytest

def task_func(data):
    try:
        username = data['username']
        password = base64.b64decode(data['password']).decode()
    except (KeyError, UnicodeDecodeError, binascii.Error, ValueError):
        return HttpResponseBadRequest('Bad Request')

    hashed_password = hashlib.sha256(password.encode()).digest()

    # Dummy authentication logic
    if username == 'admin' and hashed_password == hashlib.sha256('password'.encode()).digest():
        return HttpResponse('Login successful.')
    else:
        return HttpResponse('Login failed.', status=401)

def test_task_func_valid_input():
    data = {'username': 'admin', 'password': base64.b64encode('password'.encode()).decode()}
    response = task_func(data)
    assert response.status_code == 200
    assert response.content == b'Login successful.'

def test_task_func_invalid_input():
    data = {'username': 'admin', 'password': 'invalid_password'}
    response = task_func(data)
    assert response.status_code == 401
    assert response.content == b'Login failed.'

def test_task_func_missing_input():
    data = {'username': 'admin'}
    response = task_func(data)
    assert response.status_code == 400
    assert response.content == b'Bad Request'