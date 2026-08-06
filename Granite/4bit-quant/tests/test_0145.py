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
    ip_range = "192.168.1.0/24"
    timeout = 5
    expected_results = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
    results = task_func(ip_range, timeout)
    assert results == expected_results

def test_task_func_invalid_ip_range():
    with pytest.raises(ValueError) as e:
        ip_range = "192.168.1.0/33"  # Invalid IP range
        timeout = 5
        task_func(ip_range, timeout)
    assert "Invalid IP range" in str(e.value)

def test_task_func_connection_error():
    ip_range = "192.168.1.0/24"
    timeout = 0.1  # Low timeout to trigger connection errors
    expected_results = []
    results = task_func(ip_range, timeout)
    assert results == expected_results