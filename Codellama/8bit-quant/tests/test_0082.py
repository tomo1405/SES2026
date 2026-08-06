import pytest
from src_0082 import task_func

def test_task_func():
    api_url = 'https://example.com/api'
    template_folder = 'templates'
    app = task_func(api_url, template_folder)
    client = app.test_client()
    response = client.get('/data')
    assert response.status_code == 200
    data = response.json()
    assert data['key'] == 'value'