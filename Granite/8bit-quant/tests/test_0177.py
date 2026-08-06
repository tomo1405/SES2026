import pytest
from src_0177 import task_func

def test_task_func():
    ip_addresses = ['127.0.0.1', '8.8.8.8', 'localhost']
    expected_hostnames = {
        '127.0.0.1': 'localhost',
        '8.8.8.8': 'google-public-dns-a.google.com',
        'localhost': None
    }
    actual_hostnames = task_func(ip_addresses)
    assert actual_hostnames == expected_hostnames

def test_task_func_empty_list():
    ip_addresses = []
    expected_hostnames = {}
    actual_hostnames = task_func(ip_addresses)
    assert actual_hostnames == expected_hostnames

def test_task_func_invalid_ip():
    ip_addresses = ['not_an_ip']
    expected_hostnames = {'not_an_ip': None}
    actual_hostnames = task_func(ip_addresses)
    assert actual_hostnames == expected_hostnames