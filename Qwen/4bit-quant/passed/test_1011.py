import pytest
from src_1011 import task_func
from PIL import Image
import io
import requests
from unittest.mock import patch

def test_task_func_success():
    # Mock the requests.get method to simulate a successful response
    with patch('requests.get') as mock_get:
        # Create a mock response object
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_response.raw = io.BytesIO(b'GIF87a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x21\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;')
        mock_response.raise_for_status = lambda: None
        
        # Set the return value of the mock get method
        mock_get.return_value = mock_response
        
        # Call the function with a dummy URL
        image = task_func('http://dummy.url/image.gif')
        
        # Check if the returned object is an instance of Image.Image
        assert isinstance(image, Image.Image)

def test_task_func_failure():
    # Mock the requests.get method to simulate a failed response
    with patch('requests.get') as mock_get:
        # Set the side effect of the mock get method to raise an exception
        mock_get.side_effect = requests.exceptions.RequestException("Simulated request failure")
        
        # Call the function with a dummy URL and expect a ValueError
        with pytest.raises(ValueError) as excinfo:
            task_func('http://dummy.url/image.gif')
        
        # Check if the error message contains the expected text
        assert "Failed to retrieve image from http://dummy.url/image.gif:" in str(excinfo.value)

def test_task_func_invalid_url():
    # Test with an invalid URL that raises a ValueError
    with pytest.raises(ValueError) as excinfo:
        task_func('invalid-url')
    
    # Check if the error message contains the expected text
    assert "Failed to retrieve image from invalid-url:" in str(excinfo.value)