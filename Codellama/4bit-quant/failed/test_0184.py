import pytest
from src_0184 import task_func

def test_task_func():
    data = {'name': 'John Doe', 'age': 30}
    response = task_func(data)
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response.headers['UUID'] == str(uuid.uuid4())