python
import ipaddress
import requests
import pytest

def task_func(ip_range, timeout):
    results = []
    try:
        network = ipaddress.IPv4Network(ip_range, strict=False)  # Note the `strict=False`
    except ValueError as e:
        raise ValueError(f"Invalid IP range: {e}")

    for ip in network:
        try:
            response = requests.get(f"http://{ip}", timeout=timeout)
            if response.status_code == 200:
                results.append(str(ip))
        except requests.exceptions.ConnectionError as e:
            pass
    return results

def test_task_func():
    # Test valid IP range
    assert task_func("192.168.0.0/24", 1) == ["192.168.0.1"]

    # Test invalid IP range
    with pytest.raises(ValueError):
        task_func("192.168.0.0/33", 1)

    # Test timeout
    assert task_func("192.168.0.0/24", 0.001) == []

    # Test connection error
    assert task_func("192.168.0.0/24", 1) == ["192.168.0.1"]