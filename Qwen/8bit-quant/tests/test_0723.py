import pytest
from src_0723 import task_func
import os
import urllib.error

def test_task_func_with_valid_url(mocker):
    # Mock the urlretrieve function to simulate file download
    mock_urlretrieve = mocker.patch('src_0723.urllib.request.urlretrieve')
    
    # Mock the file content to contain the word "ERROR"
    mock_file_content = "This is an ERROR message."
    mock_open = mocker.mock_open(read_data=mock_file_content)
    mocker.patch('src_0723.open', mock_open)
    
    # Define a valid URL
    url = 'http://example.com/validfile.txt'
    
    # Call the function
    result = task_func(url)
    
    # Assert that the function returns the correct number of occurrences
    assert result == 1
    
    # Check that the file was removed after processing
    assert not os.path.exists('downloaded_file.txt')

def test_task_func_with_invalid_url(mocker):
    # Mock the urlretrieve function to raise an HTTPError
    mock_urlretrieve = mocker.patch('src_0723.urllib.request.urlretrieve')
    mock_urlretrieve.side_effect = urllib.error.HTTPError(url='http://example.com/invalidfile.txt', 
                                                        code=404, 
                                                        msg='Not Found', 
                                                        hdrs={}, 
                                                        fp=None)
    
    # Define an invalid URL
    url = 'http://example.com/invalidfile.txt'
    
    # Call the function and expect it to raise an exception
    with pytest.raises(urllib.error.HTTPError):
        task_func(url)
    
    # Check that the file was not created
    assert not os.path.exists('downloaded_file.txt')

def test_task_func_no_error_occurrences(mocker):
    # Mock the urlretrieve function to simulate file download
    mock_urlretrieve = mocker.patch('src_0723.urllib.request.urlretrieve')
    
    # Mock the file content to not contain the word "ERROR"
    mock_file_content = "This is a normal message."
    mock_open = mocker.mock_open(read_data=mock_file_content)
    mocker.patch('src_0723.open', mock_open)
    
    # Define a valid URL
    url = 'http://example.com/nomessagefile.txt'
    
    # Call the function
    result = task_func(url)
    
    # Assert that the function returns the correct number of occurrences
    assert result == 0
    
    # Check that the file was removed after processing
    assert not os.path.exists('downloaded_file.txt')