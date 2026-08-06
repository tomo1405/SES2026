import pytest
from src_0082 import task_func

def test_task_func():
    api_url = 'https://api.example.com/data'
    template_folder = 'templates'
    app = task_func(api_url, template_folder)
    client = app.test_client()
    response = client.get('/data')
    data = response.json()
    assert data == {'name': 'John Doe', 'age': 30}