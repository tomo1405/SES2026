import pytest
from src_0177 import task_func

def test_task_func():
    ip_addresses = ['192.168.1.1', '192.168.1.2', '192.168.1.3']
    expected_hostnames = {'192.168.1.1': 'host1', '192.168.1.2': 'host2', '192.168.1.3': 'host3'}
    hostnames = task_func(ip_addresses)
    assert hostnames == expected_hostnames