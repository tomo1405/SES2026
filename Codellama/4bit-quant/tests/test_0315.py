import pytest
from src_0315 import task_func

def test_task_func():
    SERVER_NAME = 'www.example.com'
    SERVER_PORT = 443
    path = '/'

    response = task_func(SERVER_NAME, SERVER_PORT, path)
    assert response.status == 200
    assert response.reason == 'OK'
    assert response.read().decode() == 'Hello, World!'