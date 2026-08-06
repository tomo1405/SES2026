import pytest
from src_0029 import task_func

def test_task_func():
    data = {"key": "value"}
    response = task_func(data)
    assert response.status_code == 200
    assert response.json() == {"payload": "encoded_data"}