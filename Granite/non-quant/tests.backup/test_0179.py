import re
import json
from src_0179 import task_func

def test_task_func_valid_ip():
    ip_address = '{"ip": "192.168.1.1"}'
    expected_output = '192.168.1.1'
    assert task_func(ip_address) == expected_output

def test_task_func_invalid_ip():
    ip_address = '{"ip": "192.168.1"}'
    expected_output = 'Invalid IP address received'
    assert task_func(ip_address) == expected_output

def test_task_func_exception():
    ip_address = '{"ip": "abc"}'
    expected_output = 'Invalid IP address received'
    assert task_func(ip_address) == expected_output