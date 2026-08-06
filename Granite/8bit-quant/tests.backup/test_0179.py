import re
import json
from src_0179 import task_func

def test_task_func_valid_ip():
    ip_address = '{"ip": "192.168.1.1"}'
    expected_output = '192.168.1.1'
    actual_output = task_func(ip_address)
    assert actual_output == expected_output

def test_task_func_invalid_ip():
    ip_address = '{"ip": "192.168.1"}'
    expected_output = 'Invalid IP address received'
    actual_output = task_func(ip_address)
    assert actual_output == expected_output

def test_task_func_exception():
    ip_address = '{"ip": "invalid_ip"}'
    expected_output = 'invalid literal for int() with base 10: \'invalid_ip\''
    actual_output = task_func(ip_address)
    assert actual_output == expected_output