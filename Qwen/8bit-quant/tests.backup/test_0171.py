import pytest
from src_0171 import task_func
import pandas as pd
from io import StringIO
import requests
from unittest.mock import patch

# Mock data for testing
MOCK_CSV_DATA = """title,year,rating
Inception,2010,8.8
Interstellar,2014,8.6
The Matrix,1999,8.7"""

@patch('requests.get')
def test_task_func(mock_get):
    # Mock the response from requests.get
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = MOCK_CSV_DATA.encode('utf-8')
    mock_get.return_value = mock_response

    # Expected DataFrame after sorting by 'title'
    expected_df = pd.DataFrame({
        'title': ['Inception', 'Interstellar', 'The Matrix'],
        'year': [2010, 2014, 1999],
        'rating': [8.8, 8.6, 8.7]
    })

    # Call the function with the mock CSV URL
    result_df = task_func('http://mock-csv-url.com')

    # Check if the result matches the expected DataFrame
    pd.testing.assert_frame_equal(result_df, expected_df)

@patch('requests.get')
def test_task_func_sort_by_year(mock_get):
    # Mock the response from requests.get
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = MOCK_CSV_DATA.encode('utf-8')
    mock_get.return_value = mock_response

    # Expected DataFrame after sorting by 'year'
    expected_df = pd.DataFrame({
        'title': ['The Matrix', 'Inception', 'Interstellar'],
        'year': [1999, 2010, 2014],
        'rating': [8.7, 8.8, 8.6]
    })

    # Call the function with the mock CSV URL and sort by 'year'
    result_df = task_func('http://mock-csv-url.com', sort_by_column='year')

    # Check if the result matches the expected DataFrame
    pd.testing.assert_frame_equal(result_df, expected_df)

@patch('requests.get')
def test_task_func_invalid_response(mock_get):
    # Mock the response from requests.get to simulate an invalid response
    mock_response = requests.Response()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    # Check if the function raises an HTTPError for invalid responses
    with pytest.raises(requests.exceptions.HTTPError):
        task_func('http://mock-csv-url.com')