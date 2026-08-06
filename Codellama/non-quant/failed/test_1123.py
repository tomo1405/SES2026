import pytest
from src_1123 import task_func

def test_task_func():
    myString = "https://www.example.com, https://www.example.org, https://www.example.net"
    expected_result = {
        "www.example.com": "192.0.2.1",
        "www.example.org": "192.0.2.2",
        "www.example.net": "192.0.2.3"
    }
    assert task_func(myString) == expected_result

def test_task_func_with_invalid_url():
    myString = "https://www.example.com, https://www.example.org, https://www.example.net, https://www.example.com/invalid"
    expected_result = {
        "www.example.com": "192.0.2.1",
        "www.example.org": "192.0.2.2",
        "www.example.net": "192.0.2.3",
        "www.example.com/invalid": None
    }
    assert task_func(myString) == expected_result

def test_task_func_with_invalid_domain():
    myString = "https://www.example.com, https://www.example.org, https://www.example.net, https://www.example.com/invalid"
    expected_result = {
        "www.example.com": "192.0.2.1",
        "www.example.org": "192.0.2.2",
        "www.example.net": "192.0.2.3",
        "www.example.com/invalid": None
    }
    assert task_func(myString) == expected_result