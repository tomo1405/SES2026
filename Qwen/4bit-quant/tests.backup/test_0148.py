import pytest
from src_0148 import task_func

def test_task_func():
    # Test with a known open port (e.g., 80) and a known closed port (e.g., 9999)
    open_port_result = task_func('127.0.0.1/32', 80)
    closed_port_result = task_func('127.0.0.1/32', 9999)

    # Assert that the correct IP address is in the result
    assert '127.0.0.1' in open_port_result
    assert '127.0.0.1' in closed_port_result

    # Assert that the port status is correctly identified
    assert open_port_result['127.0.0.1'] is True
    assert closed_port_result['127.0.0.1'] is False

def test_task_func_with_multiple_ips():
    # Test with a range of IPs and a known open port (e.g., 80)
    result = task_func('192.168.1.0/30', 80)

    # Assert that all IPs in the range are checked
    expected_ips = ['192.168.1.0', '192.168.1.1', '192.168.1.2', '192.168.1.3']
    for ip in expected_ips:
        assert ip in result

def test_task_func_invalid_ip_range():
    # Test with an invalid IP range
    with pytest.raises(ValueError):
        task_func('invalid_ip_range', 80)

def test_task_func_invalid_port():
    # Test with an invalid port number
    with pytest.raises(OSError):
        task_func('127.0.0.1/32', 65536)