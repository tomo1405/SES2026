import pytest
from src_0148 import task_func

def test_task_func():
    ip_range = "192.168.1.0/24"
    port = 80
    open_ports = task_func(ip_range, port)
    assert isinstance(open_ports, dict)
    assert all(isinstance(ip, str) for ip in open_ports.keys())
    assert all(isinstance(open, bool) for open in open_ports.values())

def test_task_func_invalid_ip_range():
    ip_range = "192.168.1.0/24"
    port = 80
    with pytest.raises(ValueError):
        task_func(ip_range, port)

def test_task_func_invalid_port():
    ip_range = "192.168.1.0/24"
    port = 80
    with pytest.raises(ValueError):
        task_func(ip_range, port)

def test_task_func_invalid_ip_range_and_port():
    ip_range = "192.168.1.0/24"
    port = 80
    with pytest.raises(ValueError):
        task_func(ip_range, port)