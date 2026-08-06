import http

import pytest
from src_0315 import task_func


def test_task_func():
    SERVER_NAME = 'example.com'
    SERVER_PORT = 443
    path = '/index.html'
    expected_output = 'Hello, World!'

    response = task_func(SERVER_NAME, SERVER_PORT, path)
    assert response == expected_output

def test_task_func_with_invalid_server_name():
    SERVER_NAME = 'invalid_server'
    SERVER_PORT = 443
    path = '/index.html'

    with pytest.raises(ConnectionError):
        task_func(SERVER_NAME, SERVER_PORT, path)

def test_task_func_with_invalid_path():
    SERVER_NAME = 'example.com'
    SERVER_PORT = 443
    path = '/invalid_path'

    with pytest.raises(http.client.BadStatusLine):
        task_func(SERVER_NAME, SERVER_PORT, path)