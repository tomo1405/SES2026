import pytest
from src_0398 import task_func

def test_task_func_valid_ip():
    API_URL = 'https://api.ipify.org?format=json'
    expected_ip = '123.456.789.10'
    assert task_func(API_URL) == expected_ip

def test_task_func_invalid_ip():
    API_URL = 'https://api.ipify.org?format=json'
    expected_ip = 'Invalid IP address received'
    assert task_func(API_URL) == expected_ip

def test_task_func_exception():
    API_URL = 'https://api.ipify.org?format=json'
    expected_exception = 'HTTPError'
    assert task_func(API_URL) == expected_exception