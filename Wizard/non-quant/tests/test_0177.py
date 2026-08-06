python
import re
import socket
import pytest

def task_func(ip_addresses: list) -> dict:
    IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'
    hostnames = {}
    for ip in ip_addresses:
        if re.match(IP_REGEX, ip):
            try:
                hostname = socket.gethostbyaddr(ip)[0]
                hostnames[ip] = hostname
            except (socket.herror, socket.gaierror):
                hostnames[ip] = None
    return hostnames

def test_task_func():
    ip_addresses = ['192.168.1.1', '10.0.0.1', 'invalid_ip', '172.16.0.1']
    expected_hostnames = {'192.168.1.1': 'hostname.local', '10.0.0.1': 'hostname.local', '172.16.0.1': None}
    assert task_func(ip_addresses) == expected_hostnames