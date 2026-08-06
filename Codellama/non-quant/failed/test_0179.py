import pytest
from src_0179 import task_func

def test_task_func_valid_ip():
    ip_address = '192.168.1.1'
    expected_ip = '192.168.1.1'
    assert task_func(ip_address) == expected_ip

def test_task_func_invalid_ip():
    ip_address = '192.168.1.1.1'
    expected_ip = 'Invalid IP address received'
    assert task_func(ip_address) == expected_ip

def test_task_func_invalid_input():
    ip_address = 'invalid_input'
    expected_ip = 'Invalid IP address received'
    assert task_func(ip_address) == expected_ip