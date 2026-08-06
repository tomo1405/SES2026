python
import re
import socket
import pytest

from src_0177 import task_func

def test_task_func():
    ip_addresses = ['192.168.1.1', '10.0.0.1', '256.0.0.1', 'localhost']
    expected_hostnames = {'192.168.1.1': 'localhost', '10.0.0.1': None, '256.0.0.1': None}
    hostnames = task_func(ip_addresses)
    assert hostnames == expected_hostnames