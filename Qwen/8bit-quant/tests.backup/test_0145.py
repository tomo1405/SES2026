import pytest
from src_0145 import task_func
import ipaddress
import requests

def test_task_func_valid_ip_range():
    ip_range = "192.168.1.0/30"
    timeout = 1
    results = task_func(ip_range, timeout)
    assert isinstance(results, list)

def test_task_func_invalid_ip_range():
    ip_range = "256.256.256.256/30"
    timeout = 1
    with pytest.raises(ValueError) as excinfo:
        task_func(ip_range, timeout)
    assert str(excinfo.value) == "Invalid IP range: invalid IPv4 address"

def test_task_func_no_active_ips(monkeypatch):
    ip_range = "192.168.1.0/30"
    timeout = 1

    def mock_get(*args, **kwargs):
        raise requests.exceptions.ConnectionError

    monkeypatch.setattr(requests, 'get', mock_get)
    results = task_func(ip_range, timeout)
    assert results == []

def test_task_func_with_active_ip(monkeypatch):
    ip_range = "192.168.1.0/30"
    timeout = 1

    def mock_get(*args, **kwargs):
        response = requests.Response()
        response.status_code = 200
        return response

    monkeypatch.setattr(requests, 'get', mock_get)
    results = task_func(ip_range, timeout)
    assert results == ['192.168.1.0', '192.168.1.1', '192.168.1.2', '192.168.1.3']