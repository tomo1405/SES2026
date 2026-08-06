import pytest
from src_0075 import task_func

def test_task_func_valid_host():
    result = task_func("example.com")
    assert "ip_address" in result
    assert "geolocation" in result

def test_task_func_invalid_host():
    with pytest.raises(ValueError):
        task_func("")

def test_task_func_network_error():
    with pytest.raises(ConnectionError):
        task_func("invalid.host")