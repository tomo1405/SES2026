from unittest.mock import patch

import pandas as pd
import pytest
import requests
from src_0391 import task_func


@patch('requests.get')
def test_task_func_valid_url(mock_get):
    # Mock the response from requests.get
    mock_response = type('MockResponse', (object,), {'text': 'title,year\nMovie A,2020\nMovie B,2019'})()
    mock_get.return_value = mock_response
    
    # Define the input dictionary with a valid URL
    csv_url_dict = {"URL": "http://example.com/data.csv"}
    
    # Call the function
    result_df = task_func(csv_url_dict)
    
    # Check if the DataFrame is sorted correctly by default column 'title'
    expected_df = pd.DataFrame({'title': ['Movie A', 'Movie B'], 'year': [2020, 2019]})
    pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df)

@patch('requests.get')
def test_task_func_invalid_url(mock_get):
    # Mock the response from requests.get to simulate a 404 error
    mock_response = type('MockResponse', (object,), {'raise_for_status': lambda: None})()
    mock_get.return_value = mock_response
    
    # Define the input dictionary with an invalid URL
    csv_url_dict = {"URL": "http://example.com/nonexistent.csv"}
    
    # Call the function and expect a ValueError
    with pytest.raises(requests.exceptions.HTTPError):
        task_func(csv_url_dict)

def test_task_func_missing_url_key():
    # Define the input dictionary without the 'URL' key
    csv_url_dict = {}
    
    # Call the function and expect a ValueError
    with pytest.raises(ValueError) as excinfo:
        task_func(csv_url_dict)
    
    # Check the error message
    assert str(excinfo.value) == "The dictionary must contain a 'URL' key."

@patch('requests.get')
def test_task_func_sort_by_column(mock_get):
    # Mock the response from requests.get
    mock_response = type('MockResponse', (object,), {'text': 'title,year\nMovie A,2020\nMovie B,2019'})()
    mock_get.return_value = mock_response
    
    # Define the input dictionary with a valid URL
    csv_url_dict = {"URL": "http://example.com/data.csv"}
    
    # Call the function with a different sort_by_column
    result_df = task_func(csv_url_dict, sort_by_column="year")
    
    # Check if the DataFrame is sorted correctly by 'year'
    expected_df = pd.DataFrame({'title': ['Movie B', 'Movie A'], 'year': [2019, 2020]})
    pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df)