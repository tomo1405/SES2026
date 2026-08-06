import pytest
from src_0081 import task_func

def test_task_func():
    template_folder = 'templates'
    app = task_func(template_folder)
    client = app.test_client()
    data = {'name': 'John Doe', 'age': 30}
    response = client.post('/', json=data)
    assert response.status_code == 200
    assert response.data == b'Hello John Doe!'