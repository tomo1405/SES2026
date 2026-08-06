from unittest.mock import MagicMock, patch

import pandas as pd
import pytest
import requests
from src_1009 import task_func


@patch('src_1009.requests.get')
def test_task_func_success(mock_get):
    # Mock the response object
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = "<html><body><table id='test_table'><tr><td>Header1</td><td>Header2</td></tr><tr><td>Data1</td><td>Data2</td></tr></table></body></html>"
    
    # Configure the mock to return the mock response
    mock_get.return_value = mock_response
    
    # Call the function
    result = task_func("http://example.com", "test_table")
    
    # Assert the result
    expected_df = pd.DataFrame({"Header1": ["Data1"], "Header2": ["Data2"]})
    pd.testing.assert_frame_equal(result, expected_df)

@patch('src_1009.requests.get')
def test_task_func_table_not_found(mock_get):
    # Mock the response object
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = "<html><body><table id='other_table'><tr><td>Header1</td><td>Header2</td></tr><tr><td>Data1</td><td>Data2</td></tr></table></body></html>"
    
    # Configure the mock to return the mock response
    mock_get.return_value = mock_response
    
    # Assert that a ValueError is raised
    with pytest.raises(ValueError) as excinfo:
        task_func("http://example.com", "test_table")
    assert str(excinfo.value) == "Table with the specified ID not found."

@patch('src_1009.requests.get')
def test_task_func_empty_table(mock_get):
    # Mock the response object
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = "<html><body><table id='test_table'></table></body></html>"
    
    # Configure the mock to return the mock response
    mock_get.return_value = mock_response
    
    # Call the function
    result = task_func("http://example.com", "test_table")
    
    # Assert the result is an empty DataFrame
    assert result.empty

@patch('src_1009.requests.get')
def test_task_func_http_error(mock_get):
    # Mock the response object to raise an HTTPError
    mock_get.side_effect = requests.exceptions.HTTPError("HTTP Error")
    
    # Assert that the HTTPError is raised
    with pytest.raises(requests.exceptions.HTTPError) as excinfo:
        task_func("http://example.com", "test_table")
    assert str(excinfo.value) == "HTTP Error"