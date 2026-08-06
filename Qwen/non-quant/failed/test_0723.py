import pytest
from unittest.mock import patch
from src_0723 import task_func
import os

@pytest.fixture
def mock_urlretrieve(mocker):
    return mocker.patch('urllib.request.urlretrieve')

@pytest.fixture
def mock_open(mocker):
    return mocker.patch('builtins.open', new_callable=mocker.mock_open)

@pytest.fixture
def mock_remove(mocker):
    return mocker.patch('os.remove')

def test_task_func(mock_urlretrieve, mock_open, mock_remove):
    # Mock the URL retrieval
    mock_urlretrieve.return_value = None
    
    # Mock file content
    mock_file_content = "This is an ERROR message.\nNo errors here."
    mock_open.return_value.read.return_value = mock_file_content
    
    # Define the URL and expected occurrences
    url = 'http://example.com'
    expected_occurrences = 1
    
    # Call the function
    result = task_func(url)
    
    # Assertions
    mock_urlretrieve.assert_called_once_with(url, 'downloaded_file.txt')
    mock_open.assert_called_once_with('downloaded_file.txt', 'r')
    mock_remove.assert_called_once_with('downloaded_file.txt')
    assert result == expected_occurrences

def test_task_func_no_errors(mock_urlretrieve, mock_open, mock_remove):
    # Mock the URL retrieval
    mock_urlretrieve.return_value = None
    
    # Mock file content
    mock_file_content = "This is a warning message.\nNo errors here."
    mock_open.return_value.read.return_value = mock_file_content
    
    # Define the URL and expected occurrences
    url = 'http://example.com'
    expected_occurrences = 0
    
    # Call the function
    result = task_func(url)
    
    # Assertions
    mock_urlretrieve.assert_called_once_with(url, 'downloaded_file.txt')
    mock_open.assert_called_once_with('downloaded_file.txt', 'r')
    mock_remove.assert_called_once_with('downloaded_file.txt')
    assert result == expected_occurrences

def test_task_func_multiple_errors(mock_urlretrieve, mock_open, mock_remove):
    # Mock the URL retrieval
    mock_urlretrieve.return_value = None
    
    # Mock file content
    mock_file_content = "This is an ERROR message.\nAnother ERROR occurred.\nNo errors here."
    mock_open.return_value.read.return_value = mock_file_content
    
    # Define the URL and expected occurrences
    url = 'http://example.com'
    expected_occurrences = 2
    
    # Call the function
    result = task_func(url)
    
    # Assertions
    mock_urlretrieve.assert_called_once_with(url, 'downloaded_file.txt')
    mock_open.assert_called_once_with('downloaded_file.txt', 'r')
    mock_remove.assert_called_once_with('downloaded_file.txt')
    assert result == expected_occurrences