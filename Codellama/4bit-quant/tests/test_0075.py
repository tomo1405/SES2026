import pytest
from src_0075 import task_func

def test_task_func_valid_host():
    host = "example.com"
    expected_ip_address = "192.0.2.1"
    expected_geolocation = {
        "ip": expected_ip_address,
        "city": "New York",
        "region": "New York",
        "country": "US",
        "loc": "40.71427,-74.00597",
        "org": "AS15169 Google LLC",
        "postal": "10001"
    }
    result = task_func(host)
    assert result["ip_address"] == expected_ip_address
    assert result["geolocation"] == expected_geolocation

def test_task_func_invalid_host():
    host = ""
    with pytest.raises(ValueError):
        task_func(host)

def test_task_func_socket_error():
    host = "example.com"
    with pytest.raises(ConnectionError):
        task_func(host)

def test_task_func_requests_error():
    host = "example.com"
    with pytest.raises(ConnectionError):
        task_func(host)