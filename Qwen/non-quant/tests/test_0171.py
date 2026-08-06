from unittest.mock import Mock, patch

import pandas as pd
import pytest
import requests
from src_0171 import task_func


def test_task_func_valid_url():
    # Mock the requests.get call to return a valid CSV response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = "title,year\nMovie A,2001\nMovie B,2000"
    
    with patch('requests.get', return_value=mock_response):
        result = task_func("http://example.com/movies.csv")
    
    expected_df = pd.DataFrame({
        'title': ['Movie B', 'Movie A'],
        'year': [2000, 2001]
    })
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_df)

def test_task_func_invalid_url():
    # Mock the requests.get call to return a 404 error
    mock_response = Mock()
    mock_response.status_code = 404
    
    with patch('requests.get', return_value=mock_response):
        with pytest.raises(requests.exceptions.HTTPError):
            task_func("http://example.com/nonexistent.csv")

def test_task_func_sort_by_year():
    # Mock the requests.get call to return a valid CSV response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = "title,year\nMovie A,2001\nMovie B,2000"
    
    with patch('requests.get', return_value=mock_response):
        result = task_func("http://example.com/movies.csv", sort_by_column="year")
    
    expected_df = pd.DataFrame({
        'title': ['Movie B', 'Movie A'],
        'year': [2000, 2001]
    })
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_df)

def test_task_func_sort_by_nonexistent_column():
    # Mock the requests.get call to return a valid CSV response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = "title,year\nMovie A,2001\nMovie B,2000"
    
    with patch('requests.get', return_value=mock_response):
        with pytest.raises(KeyError):
            task_func("http://example.com/movies.csv", sort_by_column="nonexistent_column")