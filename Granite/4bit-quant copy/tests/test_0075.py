import pytest
from src_0075 import task_func

def test_task_func():
    with pytest.raises(ValueError):
        task_func("")

    with pytest.raises(ConnectionError):
        task_func("invalid_host")

def test_task_func_valid_input():
    expected_output = {
        'ip_address': '192.168.1.1',
        'geolocation': {'city': 'New York', 'country': 'USA'}
    }
    actual_output = task_func("example.com")
    assert actual_output == expected_output