import pytest
from src_0171 import task_func
import pandas as pd

# Mocking the requests module to simulate HTTP responses
from unittest.mock import patch, Mock

@patch('requests.get')
def test_task_func(mock_get):
    # Sample CSV data
    csv_data = """title,year
The Matrix,1999
Inception,2010
Interstellar,2014"""

    # Mock the response from requests.get
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = csv_data
    mock_get.return_value = mock_response

    # URL to be used in the function call
    csv_url = "http://example.com/sample.csv"

    # Expected DataFrame after sorting by 'title'
    expected_df = pd.DataFrame({
        'title': ['Inception', 'Interstellar', 'The Matrix'],
        'year': [2010, 2014, 1999]
    })

    # Call the function
    result_df = task_func(csv_url)

    # Check if the result matches the expected DataFrame
    pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df)

@patch('requests.get')
def test_task_func_sort_by_year(mock_get):
    # Sample CSV data
    csv_data = """title,year
The Matrix,1999
Inception,2010
Interstellar,2014"""

    # Mock the response from requests.get
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = csv_data
    mock_get.return_value = mock_response

    # URL to be used in the function call
    csv_url = "http://example.com/sample.csv"

    # Expected DataFrame after sorting by 'year'
    expected_df = pd.DataFrame({
        'title': ['The Matrix', 'Inception', 'Interstellar'],
        'year': [1999, 2010, 2014]
    })

    # Call the function with 'year' as the sort column
    result_df = task_func(csv_url, sort_by_column='year')

    # Check if the result matches the expected DataFrame
    pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df)

@patch('requests.get')
def test_task_func_invalid_response(mock_get):
    # Mock the response from requests.get with a 404 status code
    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    # URL to be used in the function call
    csv_url = "http://example.com/nonexistent.csv"

    # Call the function and expect it to raise an HTTPError
    with pytest.raises(requests.exceptions.HTTPError):
        task_func(csv_url)