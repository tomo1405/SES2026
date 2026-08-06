import pytest
from src_0145 import task_func

def test_task_func_valid_ip_range():
    ip_range = "192.168.1.0/24"
    timeout = 10
    results = task_func(ip_range, timeout)
    assert len(results) > 0

def test_task_func_invalid_ip_range():
    ip_range = "192.168.1.0/33"
    timeout = 10
    with pytest.raises(ValueError):
        task_func(ip_range, timeout)

def test_task_func_timeout():
    ip_range = "192.168.1.0/24"
    timeout = 0.001
    results = task_func(ip_range, timeout)
    assert len(results) == 0