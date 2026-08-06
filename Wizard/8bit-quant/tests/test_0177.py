python
import pytest
from src_0177 import task_func

def test_task_func():
    ip_addresses = ['192.168.1.1', '10.0.0.1', 'invalid_ip', '172.16.58.3']
    expected_output = {'192.168.1.1': 'hostname1.example.com',
                       '10.0.0.1': 'hostname2.example.com',
                       'invalid_ip': None,
                       '172.16.58.3': 'hostname3.example.com'}
    assert task_func(ip_addresses) == expected_output