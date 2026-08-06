import pytest
from src_0148 import task_func

def test_task_func():
    ip_range = "192.168.1.0/24"
    port = 80
    expected_output = {
        "192.168.1.1": True,
        "192.168.1.2": False,
        "192.168.1.3": True,
        # Add more expected IP addresses and their corresponding open port status as needed
    }

    actual_output = task_func(ip_range, port)

    assert actual_output == expected_output