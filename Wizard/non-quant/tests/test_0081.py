python
import pytest
from src_0081 import task_func

def test_task_func():
    app = task_func('templates')
    client = app.test_client()
    response = client.post('/', json={'name': 'John'})
    assert response.status_code == 200
    assert b'John' in response.data