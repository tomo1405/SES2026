import pytest
from src_0274 import task_func

def test_task_func():
    handler_class = task_func()
    request = {
        'headers': {'content-type': 'application/json'},
        'body': '{"data": "test"}'
    }
    response = handler_class('request', request)
    assert response == 200