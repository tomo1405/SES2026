import pytest
from src_0182 import task_func

def test_task_func():
    # Test the task_func function
    data = "test_data"
    min_delay = 1
    max_delay = 5
    response = task_func(data, min_delay, max_delay)
    
    assert response is not None
    assert response.status_code == 200
    assert response.content == b'test_data'
    assert response.headers['Content-Type'] == 'application/json'