from unittest.mock import patch

import pandas as pd
import pytest
import requests
from src_0391 import task_func

# Mock data for testing
mock_csv_data = """title,year
Movie A,2020
Movie B,2019
Movie C,2021"""

@patch('requests.get')
def test_task_func(mock_get):
    # Setup mock response
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.text = mock_csv_data
    
    # Test with default parameters
    result_df = task_func({"URL": "http://example.com/movies.csv"})
    expected_df = pd.DataFrame({
        'title': ['Movie B', 'Movie A', 'Movie C'],
        'year': [2019, 2020, 2021]
    })
    pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df)

    # Test with sorting by 'year'
    result_df_year = task_func({"URL": "http://example.com/movies.csv"}, sort_by_column="year")
    expected_df_year = pd.DataFrame({
        'title': ['Movie B', 'Movie A', 'Movie C'],
        'year': [2019, 2020, 2021]
    })
    pd.testing.assert_frame_equal(result_df_year.reset_index(drop=True), expected_df_year)

@patch('requests.get')
def test_task_func_invalid_url(mock_get):
    # Setup mock response for invalid URL
    mock_response = mock_get.return_value
    mock_response.status_code = 404
    
    # Test with invalid URL
    with pytest.raises(requests.exceptions.HTTPError):
        task_func({"URL": "http://example.com/invalid.csv"})

def test_task_func_missing_url():
    # Test with missing 'URL' key
    with pytest.raises(ValueError):
        task_func({})

def test_task_func_empty_dict():
    # Test with empty dictionary
    with pytest.raises(ValueError):
        task_func({})