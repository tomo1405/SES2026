import pytest
from src_0081 import task_func
from flask import Flask, jsonify
import os

@pytest.fixture
def client():
    app = task_func(template_folder='templates')
    with app.test_client() as client:
        yield client

def test_handle_post(client, tmp_path):
    # Create a temporary log file
    log_file = tmp_path / "out.log"
    
    # Define test data
    test_data = {"key": "value"}
    
    # Make a POST request with JSON data
    response = client.post('/', json=test_data)
    
    # Check if the response is correct
    assert response.status_code == 200
    assert b'value' in response.data
    
    # Check if the log file contains the correct data
    assert log_file.exists()
    with open(log_file, 'r') as f:
        log_content = f.read()
        assert json.dumps(test_data) in log_content

def test_handle_post_with_invalid_json(client):
    # Make a POST request with invalid JSON data
    response = client.post('/', data='invalid json', content_type='application/json')
    
    # Check if the response is correct
    assert response.status_code == 400
    assert b'Failed to decode JSON' in response.data