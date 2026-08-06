import pytest
from src_0078 import task_func

def test_task_func_valid_input():
    data = {'username': 'admin', 'password': 'password'}
    response = task_func(data)
    assert response.status_code == 200
    assert response.content == b'Login successful.'

def test_task_func_invalid_input():
    data = {'username': 'admin', 'password': 'invalid_password'}
    response = task_func(data)
    assert response.status_code == 401
    assert response.content == b'Login failed.'

def test_task_func_missing_username():
    data = {'password': 'password'}
    response = task_func(data)
    assert response.status_code == 400
    assert response.content == b'Bad Request'

def test_task_func_missing_password():
    data = {'username': 'admin'}
    response = task_func(data)
    assert response.status_code == 400
    assert response.content == b'Bad Request'

def test_task_func_invalid_username():
    data = {'username': 'invalid_username', 'password': 'password'}
    response = task_func(data)
    assert response.status_code == 401
    assert response.content == b'Login failed.'