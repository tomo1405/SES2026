import pytest
from src_1123 import task_func

def test_task_func():
    myString = "Here is a link: https://www.example.com and another one: https://www.google.com"
    expected_output = {
        "www.example.com": "127.0.0.1",  # Assuming this is the IP address for www.example.com
        "www.google.com": "127.0.0.1"   # Assuming this is the IP address for www.google.com
    }
    actual_output = task_func(myString)
    assert actual_output == expected_output

def test_task_func_with_invalid_url():
    myString = "Here is a link: http://www.example.com and another one: https://www.google.com"
    expected_output = {
        "www.example.com": None,  # Assuming this is the expected output for an invalid URL
        "www.google.com": "127.0.0.1"
    }
    actual_output = task_func(myString)
    assert actual_output == expected_output