import pytest
from src_0081 import task_func
from flask import Flask, jsonify
from unittest.mock import patch, mock_open
import os

@pytest.fixture
def client():
    app = task_func(template_folder='templates')
    with app.test_client() as client:
        yield client

def test_handle_post(client):
    with patch('src_0081.logging') as mock_logging, \
         patch('builtins.open', new_callable=mock_open()) as mock_file:
        
        response = client.post('/', json={'key': 'value'})
        
        assert response.status_code == 200
        assert response.content_type == 'text/html'
        
        mock_logging.info.assert_called_once_with('{"key": "value"}')
        mock_file.assert_called_once_with('out.log', 'a')

def test_handle_post_invalid_json(client):
    with patch('src_0081.logging') as mock_logging:
        
        response = client.post('/', data='invalid json', content_type='application/json')
        
        assert response.status_code == 400
        assert response.content_type == 'application/json'
        assert response.json == {'error': 'Invalid JSON'}
        
        mock_logging.info.assert_not_called()

def test_handle_post_no_data(client):
    with patch('src_0081.logging') as mock_logging:
        
        response = client.post('/')
        
        assert response.status_code == 400
        assert response.content_type == 'application/json'
        assert response.json == {'error': 'No data provided'}
        
        mock_logging.info.assert_not_called()