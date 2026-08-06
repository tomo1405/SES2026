from unittest.mock import MagicMock, patch

import pandas as pd
import pytest
import requests
from src_0995 import task_func


@patch('src_0995.requests.get')
def test_task_func_success(mock_get):
    # Mock the response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = """
    <html>
        <body>
            <div class="container">
                <h1>Title 1</h1>
                <span class="date">2023-10-01</span>
                <span class="author">Author 1</span>
            </div>
            <div class="container">
                <h1>Title 2</h1>
                <span class="date">2023-10-02</span>
                <span class="author">Author 2</span>
            </div>
        </body>
    </html>
    """
    mock_get.return_value = mock_response

    # Define inputs and expected output
    url = "http://example.com"
    csv_file_path = "test_output.csv"
    expected_data = [
        ("Title 1", "2023-10-01", "Author 1"),
        ("Title 2", "2023-10-02", "Author 2")
    ]

    # Call the function
    result = task_func(url, csv_file_path)

    # Assert the result
    assert result == expected_data

    # Check if the CSV file was written correctly
    df = pd.read_csv(csv_file_path)
    assert df.equals(pd.DataFrame(expected_data, columns=["Title", "Date", "Author"]))

@patch('src_0995.requests.get')
def test_task_func_no_data(mock_get):
    # Mock the response with no data
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = "<html><body></body></html>"
    mock_get.return_value = mock_response

    # Define inputs and expected output
    url = "http://example.com"
    csv_file_path = "test_output.csv"
    expected_data = [("No Title", "No Date", "No Author")]

    # Call the function
    result = task_func(url, csv_file_path)

    # Assert the result
    assert result == expected_data

    # Check if the CSV file was written correctly
    df = pd.read_csv(csv_file_path)
    assert df.equals(pd.DataFrame(expected_data, columns=["Title", "Date", "Author"]))

@patch('src_0995.requests.get')
def test_task_func_request_exception(mock_get):
    # Mock the request to raise an exception
    mock_get.side_effect = requests.RequestException("Connection error")

    # Define inputs
    url = "http://example.com"
    csv_file_path = "test_output.csv"

    # Assert that a RuntimeError is raised
    with pytest.raises(RuntimeError) as excinfo:
        task_func(url, csv_file_path)

    # Check the error message
    assert str(excinfo.value) == "Error fetching URL: Connection error"