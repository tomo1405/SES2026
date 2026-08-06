import pytest
from src_0724 import task_func
import os
import csv

# Mocking the urllib.request.urlopen to avoid network calls
from unittest.mock import patch, mock_open

@pytest.fixture
def mock_html():
    return """
    <html>
        <body>
            <table class="data-table">
                <tr><td>Header 1</td><td>Header 2</td></tr>
                <tr><td>Data 1</td><td>Data 2</td></tr>
            </table>
        </body>
    </html>
    """

@pytest.fixture
def mock_csv_file_path():
    return 'scraped_data.csv'

@patch('src_0724.urllib.request.urlopen')
@patch('builtins.open', new_callable=mock_open)
def test_task_func(mock_urlopen, mock_file, mock_html, mock_csv_file_path):
    # Mock the response from urlopen
    mock_response = mock.Mock()
    mock_response.read.return_value = mock_html.encode('utf-8')
    mock_urlopen.return_value = mock_response

    # Call the function
    result = task_func('http://example.com')

    # Check if the CSV file was written correctly
    assert result == mock_csv_file_path

    # Check if the CSV file content is as expected
    handle = mock_file()
    handle.write.assert_called_once_with('Header 1,Header 2\nData 1,Data 2\n')

    # Check if the file was opened in write mode
    mock_file.assert_called_once_with(mock_csv_file_path, 'w')

    # Clean up the CSV file after the test
    if os.path.exists(mock_csv_file_path):
        os.remove(mock_csv_file_path)