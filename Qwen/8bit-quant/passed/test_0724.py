import pytest
from src_0724 import task_func
import os
import csv

# Mocking dependencies
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_urlopen():
    with patch('urllib.request.urlopen') as mock:
        mock.return_value.read.return_value = b'<html><body><table class="data-table"><tr><td>Row1-Col1</td><td>Row1-Col2</td></tr><tr><td>Row2-Col1</td><td>Row2-Col2</td></tr></table></body></html>'
        yield mock

@pytest.fixture
def mock_os_path_exists():
    with patch('os.path.exists') as mock:
        mock.return_value = True
        yield mock

@pytest.fixture
def mock_os_remove():
    with patch('os.remove') as mock:
        yield mock

@pytest.fixture
def mock_csv_writer():
    with patch('csv.writer') as mock:
        yield mock

def test_task_func(mock_urlopen, mock_os_path_exists, mock_os_remove, mock_csv_writer):
    url = 'http://example.com'
    expected_csv_path = 'scraped_data.csv'
    
    result = task_func(url)
    
    assert result == expected_csv_path
    
    # Verify that urlopen was called with the correct URL
    mock_urlopen.assert_called_once_with(url)
    
    # Verify that os.path.exists was called with the correct file path
    mock_os_path_exists.assert_called_once_with(expected_csv_path)
    
    # Verify that os.remove was called with the correct file path
    mock_os_remove.assert_called_once_with(expected_csv_path)
    
    # Verify that csv.writer was called and writerows was called with the correct data
    mock_csv_writer.assert_called_once()
    writer = mock_csv_writer()
    writer.writerows.assert_called_once_with([['Row1-Col1', 'Row1-Col2'], ['Row2-Col1', 'Row2-Col2']])