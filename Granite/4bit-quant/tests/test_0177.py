import pytest
from src_0177 import task_func

def test_task_func():
    ip_addresses = ['192.168.1.1', '10.0.0.1', '2001:0db8:85a3:0000:0000:8a2e:0370:7334']
    expected_output = {
        '192.168.1.1': 'example.com',
        '10.0.0.1': 'another-example.com',
        '2001:0db8:85a3:0000:0000:8a2e:0370:7334': ' yet-another-example.com'
    }
    actual_output = task_func(ip_addresses)
    assert actual_output == expected_output

def test_task_func_with_invalid_ip():
    ip_addresses = ['192.168.1.1', 'invalid_ip', '2001:0db8:85a3:0000:0000:8a2e:0370:7334']
    expected_output = {
        '192.168.1.1': 'example.com',
        '2001:0db8:85a3:0000:0000:8a2e:0370:7334': 'yet-another-example.com'
    }
    actual_output = task_func(ip_addresses)
    assert actual_output == expected_output