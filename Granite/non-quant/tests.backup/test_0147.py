import pytest
from src_0147 import task_func

def test_task_func():
    active_ips = task_func('192.168.1.0/24')
    assert isinstance(active_ips, dict)
    for ip, status in active_ips.items():
        assert isinstance(ip, str)
        assert isinstance(status, bool)