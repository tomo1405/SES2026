import pytest
from src_0422 import task_func
import os
import tempfile
import requests
import json

@pytest.fixture
def mock_requests_post(monkeypatch):
    def mock_post(url, files, headers, data):
        response = requests.Response()
        response.status_code = 200
        return response

    monkeypatch.setattr(requests, 'post', mock_post)

def test_task_func_with_files(mock_requests_post):
    # Create a temporary directory and add some files
    with tempfile.TemporaryDirectory() as temp_dir:
        for i in range(3):
            with open(os.path.join(temp_dir, f'file_{i}.txt'), 'w') as f:
                f.write('Sample content')

        url = 'http://example.com/upload'
        metadata = {'key': 'value'}

        # Call the function
        status_codes = task_func(url, temp_dir, metadata)

        # Assert the number of status codes returned is equal to the number of files
        assert len(status_codes) == 3

        # Assert all status codes are 200
        assert all(code == 200 for code in status_codes)

def test_task_func_no_files(mock_requests_post):
    # Create a temporary directory without any files
    with tempfile.TemporaryDirectory() as temp_dir:

        url = 'http://example.com/upload'
        metadata = {'key': 'value'}

        # Call the function
        status_codes = task_func(url, temp_dir, metadata)

        # Assert no status codes are returned
        assert status_codes == []

def test_task_func_non_existent_directory():
    url = 'http://example.com/upload'
    metadata = {'key': 'value'}
    non_existent_dir = '/non/existent/directory'

    # Call the function
    with pytest.raises(FileNotFoundError):
        task_func(url, non_existent_dir, metadata)