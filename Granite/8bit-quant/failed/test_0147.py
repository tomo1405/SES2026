import pytest
from src_0147 import task_func

def test_task_func():
    ip_range = '192.168.1.0/24'
    expected_output = {
        '192.168.1.1': True,
        '192.168.1.2': True,
        '192.168.1.255': True,
    }
    actual_output = task_func(ip_range)
    assert actual_output == expected_output

def test_task_func_with_empty_range():
    ip_range = '10.0.0.0/32'
    expected_output = {
        '10.0.0.0': True,
    }
    actual_output = task_func(ip_range)
    assert actual_output == expected_output

def test_task_func_with_invalid_ip_range():
    ip_range = '123.456.789.0/24'
    with pytest.raises(ValueError):
        task_func(ip_range)