python
import ipaddress
import requests
import pytest

def task_func(ip_range, timeout):
    results = []
    try:
        network = ipaddress.IPv4Network(ip_range, strict=False)
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
    ip_range = "192.168.0.0/24"
    timeout = 1
    assert task_func(ip_range, timeout) == ["192.168.0.1", "192.168.0.2", "192.168.0.3"]

    # Test invalid IP range
    ip_range = "192.168.0.0/33"
    timeout = 1
    with pytest.raises(ValueError):
        task_func(ip_range, timeout)

    # Test timeout
    ip_range = "192.168.0.0/24"
    timeout = 0.001
    with pytest.raises(requests.exceptions.Timeout):
        task_func(ip_range, timeout)