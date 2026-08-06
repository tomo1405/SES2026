import pytest
from src_1123 import task_func

def test_task_func():
    myString = "https://www.google.com https://www.facebook.com http://www.invalid.com"
    expected_output = {
        "www.google.com": "172.217.12.142",
        "www.facebook.com": "31.13.71.36",
        "www.invalid.com": None
    }
    assert task_func(myString) == expected_output

def test_task_func_empty_string():
    myString = ""
    expected_output = {}
    assert task_func(myString) == expected_output

def test_task_func_no_urls():
    myString = "This is a string with no URLs"
    expected_output = {}
    assert task_func(myString) == expected_output

def test_task_func_invalid_url():
    myString = "https://www.google.com https://www.facebook.com invalid_url"
    expected_output = {
        "www.google.com": "172.217.12.142",
        "www.facebook.com": "31.13.71.36",
    }
    assert task_func(myString) == expected_output