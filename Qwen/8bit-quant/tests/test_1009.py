from unittest.mock import patch

import pandas as pd
import pytest
import requests
from src_1009 import task_func


# Mocking the requests module to simulate HTTP responses
@patch('src_1009.requests.get')
def test_task_func_success(mock_get):
    # Mock response with a simple HTML content containing a table
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.text = """
    <html>
    <body>
    <table id="example_table">
        <tr><th>Header1</th><th>Header2</th></tr>
        <tr><td>Data1</td><td>Data2</td></tr>
    </table>
    </body>
    </html>
    """

    # Expected DataFrame
    expected_df = pd.DataFrame({
        'Header1': ['Data1'],
        'Header2': ['Data2']
    })

    # Call the function and assert the result
    result_df = task_func("http://example.com", "example_table")
    pd.testing.assert_frame_equal(result_df, expected_df)

@patch('src_1009.requests.get')
def test_task_func_no_table(mock_get):
    # Mock response with HTML content but no table with the specified ID
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.text = "<html><body></body></html>"

    # Assert that a ValueError is raised
    with pytest.raises(ValueError, match="Table with the specified ID not found."):
        task_func("http://example.com", "nonexistent_table")

@patch('src_1009.requests.get')
def test_task_func_empty_table(mock_get):
    # Mock response with an empty table
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.text = """
    <html>
    <body>
    <table id="empty_table"></table>
    </body>
    </html>
    """

    # Expected empty DataFrame
    expected_df = pd.DataFrame()

    # Call the function and assert the result
    result_df = task_func("http://example.com", "empty_table")
    pd.testing.assert_frame_equal(result_df, expected_df)

@patch('src_1009.requests.get')
def test_task_func_http_error(mock_get):
    # Mock response with an HTTP error
    mock_response = mock_get.return_value
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("HTTP Error 404")

    # Assert that the HTTPError is raised
    with pytest.raises(requests.exceptions.HTTPError, match="HTTP Error 404"):
        task_func("http://example.com", "example_table")