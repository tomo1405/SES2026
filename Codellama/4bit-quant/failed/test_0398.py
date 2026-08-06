import pytest
from src_0398 import task_func

def test_task_func():
    # Test with valid IP address
    API_URL = 'https://api.ipify.org?format=json'
    expected_ip = '123.456.789.012'
    assert task_func(API_URL) == expected_ip

    # Test with invalid IP address
    API_URL = 'https://api.ipify.org?format=json'
    expected_error = 'Invalid IP address received'
    assert task_func(API_URL) == expected_error

    # Test with invalid URL
    API_URL = 'https://api.ipify.org?format=json'
    expected_error = 'Invalid URL'
    assert task_func(API_URL) == expected_error