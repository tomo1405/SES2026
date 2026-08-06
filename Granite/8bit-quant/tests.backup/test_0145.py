import ipaddress
import pytest
import requests
from src_0145 import task_func

def test_task_func():
    ip_range = "192.168.1.0/24"
    timeout = 5
    expected_results = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

    results = task_func(ip_range, timeout)

    assert results == expected_results

def test_task_func_invalid_ip_range():
    ip_range = "192.168.1.0/33"  # Invalid IP range
    timeout = 5

    with pytest.raises(ValueError) as e:
        task_func(ip_range, timeout)

    assert "Invalid IP range" in str(e.value)

def test_task_func_connection_error():
    ip_range = "192.168.1.0/24"
    timeout = 5
    expected_results = ["192.168.1.1", "192.168.1.2"]

    def mock_get(*args, **kwargs):
        raise requests.exceptions.ConnectionError("Mock connection error")

    with pytest.patch("requests.get", side_effect=mock_get):
        results = task_func(ip_range, timeout)

    assert results == expected_results