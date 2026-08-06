import logging
import os

import pytest
from src_0081 import task_func


@pytest.fixture
def client():
    # Create a temporary directory for templates
    template_dir = os.path.join(os.getcwd(), 'templates')
    os.makedirs(template_dir, exist_ok=True)
    
    # Create a simple index.html template
    with open(os.path.join(template_dir, 'index.html'), 'w') as f:
        f.write("{{ data }}")
    
    app = task_func(template_dir)
    app.config['TESTING'] = True
    
    with app.test_client() as client:
        yield client
    
    # Clean up the temporary directory
    os.rmdir(template_dir)

def test_handle_post(client):
    response = client.post('/', json={'key': 'value'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == '{"key": "value"}'

def test_logging(client, caplog):
    with caplog.at_level(logging.INFO):
        client.post('/', json={'key': 'value'})
        assert len(caplog.records) == 1
        assert caplog.records[0].levelname == 'INFO'
        assert caplog.records[0].message == '{"key": "value"}'