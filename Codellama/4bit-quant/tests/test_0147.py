import pytest
from src_0147 import task_func

def test_task_func():
    ip_range = '192.168.1.0/24'
    active_ips = task_func(ip_range)
    assert len(active_ips) == 256
    assert all(isinstance(ip, str) for ip in active_ips)
    assert all(ip.startswith('192.168.1.') for ip in active_ips)
    assert all(ip.endswith('/24') for ip in active_ips)
    assert all(isinstance(active_ips[ip], bool) for ip in active_ips)