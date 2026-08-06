import pytest
from src_0184 import task_func

def test_task_func():
    data = {'key': 'value'}
    response = task_func(data)
    assert response.status_code == 200
    assert response['Content-Type'] == 'application/json'
    assert response.content == b'{"key": "value"}'
    assert response['UUID'] == str(uuid.uuid4())