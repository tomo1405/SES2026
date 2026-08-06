import pytest
from src_0179 import task_func

def test_task_func_valid_ip():
    ip_address = '{"ip": "192.168.0.1"}'
    expected_result = '192.168.0.1'
    assert task_func(ip_address) == expected_result

def test_task_func_invalid_ip():
    ip_address = '{"ip": "192.168.0.1.2"}'
    expected_result = 'Invalid IP address received'
    assert task_func(ip_address) == expected_result

def test_task_func_invalid_json():
    ip_address = '{"ip": "192.168.0.1"'
    expected_result = 'Expecting value: line 1 column 1 (char 0)'
    assert task_func(ip_address) == expected_result