import pytest
from src_0075 import task_func

def test_task_func_valid_host():
    host = "example.com"
    result = task_func(host)
    assert result["ip_address"] == "192.0.2.1"
    assert result["geolocation"] == {
        "city": "London",
        "country": "United Kingdom",
        "region": "England"
    }

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