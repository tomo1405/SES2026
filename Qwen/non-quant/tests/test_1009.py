from unittest.mock import MagicMock, patch

import pandas as pd
import pytest
import requests
from src_1009 import task_func


# Mocking requests.get to simulate HTTP responses
@patch('src_1009.requests.get')
def test_task_func_success(mock_get):
    # Prepare mock response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = """
    <html>
        <body>
            <table id="test_table">
                <tr><th>Header1</th><th>Header2</th></tr>
                <tr><td>Data1</td><td>Data2</td></tr>
            </table>
        </body>
    </html>
    """
    mock_get.return_value = mock_response

    # Call the function
    df = task_func("http://example.com", "test_table")

    # Check if the DataFrame is correct
    expected_df = pd.DataFrame({
        'Header1': ['Data1'],
        'Header2': ['Data2']
    })
    pd.testing.assert_frame_equal(df, expected_df)

@patch('src_1009.requests.get')
def test_task_func_http_error(mock_get):
    # Prepare mock response to simulate HTTP error
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    # Call the function and expect an HTTPError
    with pytest.raises(requests.exceptions.HTTPError):
        task_func("http://example.com", "test_table")

@patch('src_1009.requests.get')
def test_task_func_table_not_found(mock_get):
    # Prepare mock response with no table
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = "<html><body></body></html>"
    mock_get.return_value = mock_response

    # Call the function and expect a ValueError
    with pytest.raises(ValueError) as excinfo:
        task_func("http://example.com", "test_table")
    assert str(excinfo.value) == "Table with the specified ID not found."

@patch('src_1009.requests.get')
def test_task_func_empty_table(mock_get):
    # Prepare mock response with an empty table
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = """
    <html>
        <body>
            <table id="test_table"></table>
        </body>
    </html>
    """
    mock_get.return_value = mock_response

    # Call the function
    df = task_func("http://example.com", "test_table")

    # Check if the DataFrame is empty
    assert df.empty