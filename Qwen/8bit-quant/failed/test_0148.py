import pytest
from src_0148 import task_func

def test_task_func_single_ip():
    ip_range = "127.0.0.1/32"
    port = 80
    result = task_func(ip_range, port)
    assert isinstance(result, dict)
    assert "127.0.0.1" in result
    assert isinstance(result["127.0.0.1"], bool)

def test_task_func_multiple_ips():
    ip_range = "192.168.1.0/30"
    port = 22
    result = task_func(ip_range, port)
    assert isinstance(result, dict)
    assert len(result) == 4
    for ip in IPv4Network(ip_range):
        assert str(ip) in result
        assert isinstance(result[str(ip)], bool)

def test_task_func_nonexistent_port():
    ip_range = "127.0.0.1/32"
    port = 9999  # Assuming this port is not open on localhost
    result = task_func(ip_range, port)
    assert isinstance(result, dict)
    assert "127.0.0.1" in result
    assert result["127.0.0.1"] is False

def test_task_func_invalid_ip_range():
    with pytest.raises(ValueError):
        task_func("invalid_ip_range", 80)

def test_task_func_invalid_port():
    ip_range = "127.0.0.1/32"
    with pytest.raises(OSError):
        task_func(ip_range, -1)

def test_task_func_large_ip_range():
    ip_range = "10.0.0.0/8"
    port = 80
    result = task_func(ip_range, port)
    assert isinstance(result, dict)
    assert len(result) == 2**24
    for ip in IPv4Network(ip_range):
        assert str(ip) in result
        assert isinstance(result[str(ip)], bool)