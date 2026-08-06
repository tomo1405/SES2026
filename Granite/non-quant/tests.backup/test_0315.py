import pytest
from src_0315 import task_func

def test_task_func():
    SERVER_NAME = 'example.com'
    SERVER_PORT = 443
    path = '/index.html'
    expected_output = b'Hello, world!'

    response = task_func(SERVER_NAME, SERVER_PORT, path)

    assert response == expected_output