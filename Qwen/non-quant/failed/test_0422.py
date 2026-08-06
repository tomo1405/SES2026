import pytest
from src_0422 import task_func
import requests
import os
import json
import time
from unittest.mock import patch, mock_open

@pytest.fixture
def mock_directory(tmpdir):
    # Create a temporary directory and add some files to it
    dir_path = tmpdir.mkdir("test_dir")
    dir_path.join("file1.txt").write("content1")
    dir_path.join("file2.txt").write("content2")
    return str(dir_path)

@pytest.fixture
def mock_url():
    return "http://mock.url"

@pytest.fixture
def mock_metadata():
    return {"key": "value"}

@patch('requests.post')
@patch('os.listdir')
@patch('os.path.isfile')
def test_task_func(mock_isfile, mock_listdir, mock_post, mock_directory, mock_url, mock_metadata):
    # Mock os.listdir to return the files in the directory
    mock_listdir.return_value = ["file1.txt", "file2.txt"]
    
    # Mock os.path.isfile to always return True
    mock_isfile.return_value = True
    
    # Mock the response from requests.post
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_post.return_value = mock_response
    
    # Call the function
    result = task_func(mock_url, mock_directory, mock_metadata)
    
    # Assert that requests.post was called twice (once for each file)
    assert mock_post.call_count == 2
    
    # Assert that the correct files were sent in the request
    expected_files = [
        {'file': ('file1.txt', b'content1', 'text/plain')},
        {'file': ('file2.txt', b'content2', 'text/plain')}
    ]
    for i, call in enumerate(mock_post.call_args_list):
        assert call[1]['files'] == expected_files[i]
    
    # Assert that the correct metadata was sent in the request
    for call in mock_post.call_args_list:
        assert call[1]['data'] == json.dumps(mock_metadata)
    
    # Assert that the correct headers were used
    for call in mock_post.call_args_list:
        assert call[1]['headers'] == {'accept': 'text/json', 'Content-Type': 'application/json'}
    
    # Assert that the function returned the correct status codes
    assert result == [200, 200]

@patch('os.listdir')
def test_task_func_no_files(mock_listdir, mock_directory, mock_url, mock_metadata):
    # Mock os.listdir to return no files
    mock_listdir.return_value = []
    
    # Call the function
    result = task_func(mock_url, mock_directory, mock_metadata)
    
    # Assert that the function returned an empty list
    assert result == []

@patch('os.listdir')
@patch('os.path.isfile')
def test_task_func_non_file(mock_isfile, mock_listdir, mock_directory, mock_url, mock_metadata):
    # Mock os.listdir to return a non-file item
    mock_listdir.return_value = ["file1.txt", "nonfile"]
    
    # Mock os.path.isfile to return False for the non-file item
    mock_isfile.side_effect = [True, False]
    
    # Call the function
    result = task_func(mock_url, mock_directory, mock_metadata)
    
    # Assert that the function returned an empty list
    assert result == []