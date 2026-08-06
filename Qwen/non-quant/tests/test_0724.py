import pytest
from unittest.mock import patch, mock_open
from src_0724 import task_func

# Constants
CSV_FILE_PATH = 'scraped_data.csv'

@pytest.fixture
def mock_url():
    return "http://example.com"

@pytest.fixture
def mock_html():
    return b"""
    <html>
        <body>
            <table class="data-table">
                <tr><td>Row1-Col1</td><td>Row1-Col2</td></tr>
                <tr><td>Row2-Col1</td><td>Row2-Col2</td></tr>
            </table>
        </body>
    </html>
    """

@pytest.fixture
def mock_csv_data():
    return [
        ['Row1-Col1', 'Row1-Col2'],
        ['Row2-Col1', 'Row2-Col2']
    ]

@patch('urllib.request.urlopen')
@patch('csv.writer')
def test_task_func(mock_writer, mock_urlopen, mock_url, mock_html, mock_csv_data):
    # Mock the urlopen to return the mock HTML
    mock_response = mock_urlopen.return_value
    mock_response.read.return_value = mock_html
    
    # Mock the csv.writer to capture the written data
    mock_csv_writer = mock_writer.return_value
    mock_csv_writer.writerows = lambda rows: None  # No-op for writerows
    
    # Call the function
    result = task_func(mock_url)
    
    # Assert the result is the correct file path
    assert result == CSV_FILE_PATH
    
    # Assert the csv.writer was called with the correct data
    mock_csv_writer.writerows.assert_called_once_with(mock_csv_data)

@patch('os.path.exists')
@patch('os.remove')
def test_file_cleanup(mock_remove, mock_exists, mock_url, mock_html):
    # Mock the file existence to True
    mock_exists.return_value = True
    
    # Call the function
    task_func(mock_url)
    
    # Assert that os.remove was called
    mock_remove.assert_called_once_with(CSV_FILE_PATH)