import pytest
from src_0078 import task_func
from django.http import HttpResponseBadRequest, HttpResponse

def test_task_func_missing_username():
    response = task_func({'password': 'cGFzc3dvcmQ='})
    assert isinstance(response, HttpResponseBadRequest)
    assert response.content == b'Bad Request'

def test_task_func_missing_password():
    response = task_func({'username': 'admin'})
    assert isinstance(response, HttpResponseBadRequest)
    assert response.content == b'Bad Request'

def test_task_func_invalid_base64_password():
    response = task_func({'username': 'admin', 'password': 'invalid_base64'})
    assert isinstance(response, HttpResponseBadRequest)
    assert response.content == b'Bad Request'

def test_task_func_successful_login():
    response = task_func({'username': 'admin', 'password': 'cGFzc3dvcmQ='})
    assert isinstance(response, HttpResponse)
    assert response.content == b'Login successful.'

def test_task_func_failed_login():
    response = task_func({'username': 'admin', 'password': 'cGFzc3dvcmQxMjM='})
    assert isinstance(response, HttpResponse)
    assert response.content == b'Login failed.'
    assert response.status_code == 401

def test_task_func_wrong_username():
    response = task_func({'username': 'user', 'password': 'cGFzc3dvcmQ='})
    assert isinstance(response, HttpResponse)
    assert response.content == b'Login failed.'
    assert response.status_code == 401