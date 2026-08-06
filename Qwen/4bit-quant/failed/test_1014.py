import pytest
from unittest.mock import patch, mock_open
from io import StringIO
from src_1014 import task_func

def test_task_func_with_mocked_requests():
    # Mocking the requests.get call
    mock_response = mock_open(read_data="<html><body><a href='/test'>Test</a></body></html>")
    
    with patch('src_1014.requests.get', return_value=mock_response):
        with patch('src_1014.csv.writer') as mock_csv_writer:
            result = task_func("/path/to/page")
            
            # Assert that the function returns the correct number of links
            assert result == 1
            
            # Assert that the CSV file was written correctly
            mock_csv_writer.assert_called_once()
            mock_csv_writer.return_value.writerow.assert_called_once_with(['https://www.example.com/test'])

def test_task_func_with_no_links():
    # Mocking the requests.get call with no links
    mock_response = mock_open(read_data="<html><body></body></html>")
    
    with patch('src_1014.requests.get', return_value=mock_response):
        with patch('src_1014.csv.writer') as mock_csv_writer:
            result = task_func("/path/to/empty_page")
            
            # Assert that the function returns 0 links
            assert result == 0
            
            # Assert that the CSV file was not written
            mock_csv_writer.assert_not_called()

def test_task_func_with_multiple_links():
    # Mocking the requests.get call with multiple links
    mock_response = mock_open(read_data="<html><body><a href='/test1'>Test 1</a><a href='/test2'>Test 2</a></body></html>")
    
    with patch('src_1014.requests.get', return_value=mock_response):
        with patch('src_1014.csv.writer') as mock_csv_writer:
            result = task_func("/path/to/multiple_links_page")
            
            # Assert that the function returns the correct number of links
            assert result == 2
            
            # Assert that the CSV file was written correctly
            mock_csv_writer.assert_called_once()
            mock_csv_writer.return_value.writerow.assert_has_calls([
                pytest.call(['https://www.example.com/test1']),
                pytest.call(['https://www.example.com/test2'])
            ], any_order=True)

def test_task_func_with_base_url():
    # Mocking the requests.get call with a custom base URL
    mock_response = mock_open(read_data="<html><body><a href='/test'>Test</a></body></html>")
    
    with patch('src_1014.requests.get', return_value=mock_response):
        with patch('src_1014.csv.writer') as mock_csv_writer:
            result = task_func("/path/to/page", base_url="https://custom-base-url.com")
            
            # Assert that the function returns the correct number of links
            assert result == 1
            
            # Assert that the CSV file was written correctly with the custom base URL
            mock_csv_writer.assert_called_once()
            mock_csv_writer.return_value.writerow.assert_called_once_with(['https://custom-base-url.com/test'])

def test_task_func_with_custom_csv_file():
    # Mocking the requests.get call and specifying a custom CSV file
    mock_response = mock_open(read_data="<html><body><a href='/test'>Test</a></body></html>")
    
    with patch('src_1014.requests.get', return_value=mock_response):
        with patch('src_1014.csv.writer') as mock_csv_writer:
            result = task_func("/path/to/page", csv_file="custom_scraped_data.csv")
            
            # Assert that the function returns the correct number of links
            assert result == 1
            
            # Assert that the CSV file was written correctly with the custom file name
            mock_csv_writer.assert_called_once()
            mock_csv_writer.return_value.writerow.assert_called_once_with(['https://www.example.com/test'])