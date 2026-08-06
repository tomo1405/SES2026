import pytest
from src_1123 import task_func

def test_task_func():
    myString = "https://www.example.com, https://www.example2.com"
    expected_result = {"www.example.com": "123.123.123.123", "www.example2.com": "456.456.456.456"}
    assert task_func(myString) == expected_result

def test_task_func_invalid_url():
    myString = "https://www.example.com, https://www.example2.com, https://www.example3.com"
    expected_result = {"www.example.com": "123.123.123.123", "www.example2.com": "456.456.456.456", "www.example3.com": None}
    assert task_func(myString) == expected_result

def test_task_func_invalid_domain():
    myString = "https://www.example.com, https://www.example2.com, https://www.example3.com"
    expected_result = {"www.example.com": "123.123.123.123", "www.example2.com": "456.456.456.456", "www.example3.com": None}
    assert task_func(myString) == expected_result