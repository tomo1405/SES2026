import pytest
from src_0145 import task_func

def test_task_func_valid_ip_range():
    ip_range = "192.168.1.0/24"
    timeout = 5
    results = task_func(ip_range, timeout)
    assert results == ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

def test_task_func_invalid_ip_range():
    ip_range = "192.168.1.0/33"
    timeout = 5
    with pytest.raises(ValueError):
        task_func(ip_range, timeout)

def test_task_func_timeout():
    ip_range = "192.168.1.0/24"
    timeout = 0.001
    results = task_func(ip_range, timeout)
    assert results == []

def test_task_func_valid_ip_range_with_timeout():
    ip_range = "192.168.1.0/24"
    timeout = 5
    results = task_func(ip_range, timeout)
    assert results == ["192.168.1.1", "192.168.1.2", "192.168.1.3"]