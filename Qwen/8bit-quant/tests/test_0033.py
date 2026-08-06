import pytest
from src_0033 import task_func
from unittest.mock import patch
from bs4 import BeautifulSoup

@patch('requests.get')
def test_task_func(mock_get):
    # Mock the response from requests.get
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.text = "<html><body><h1>Test Content</h1></body></html>"
    
    # Create a BeautifulSoup object with the mocked response text
    soup = BeautifulSoup(mock_response.text, 'html.parser')
    
    # Mock the find method of BeautifulSoup to return a tag
    mock_tag = soup.find('h1')
    
    # Call the function with the mocked URL and tag
    result = task_func('http://test.com', 'h1')
    
    # Assert that the result is the string content of the tag
    assert result == "Test Content"

@patch('requests.get')
def test_task_func_no_tag(mock_get):
    # Mock the response from requests.get
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.text = "<html><body></body></html>"
    
    # Create a BeautifulSoup object with the mocked response text
    soup = BeautifulSoup(mock_response.text, 'html.parser')
    
    # Mock the find method of BeautifulSoup to return None
    mock_tag = soup.find('h1')
    
    # Call the function with the mocked URL and tag
    result = task_func('http://test.com', 'h1')
    
    # Assert that the result is None
    assert result is None

@patch('requests.get')
def test_task_func_non_200_status(mock_get):
    # Mock the response from requests.get
    mock_response = mock_get.return_value
    mock_response.status_code = 404
    
    # Call the function with the mocked URL and tag
    result = task_func('http://test.com', 'h1')
    
    # Assert that the result is None due to non-200 status code
    assert result is None