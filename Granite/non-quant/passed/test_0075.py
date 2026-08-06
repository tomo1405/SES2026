import pytest
from src_0075 import task_func

def test_task_func():
    with pytest.raises(ValueError):
        task_func("")

    with pytest.raises(ConnectionError):
        task_func("invalid-host")

    result = task_func("google.com")
    assert 'ip_address' in result
    assert 'geolocation' in result