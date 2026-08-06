import pytest
from src_1123 import task_func

def test_task_func_no_urls():
    input_string = "No URLs here!"
    expected_output = {}
    assert task_func(input_string) == expected_output

def test_task_func_single_url_resolvable():
    input_string = "Check out this website: https://www.example.com"
    expected_output = {"www.example.com": "93.184.216.34"}  # Example IP, may change
    assert task_func(input_string) == expected_output

def test_task_func_single_url_unresolvable():
    input_string = "Check out this website: https://nonexistentdomain123.com"
    expected_output = {"nonexistentdomain123.com": None}
    assert task_func(input_string) == expected_output

def test_task_func_multiple_urls():
    input_string = "Visit https://www.example.com or http://www.google.com"
    expected_output = {
        "www.example.com": "93.184.216.34",  # Example IP, may change
        "www.google.com": "172.217.16.196"   # Example IP, may change
    }
    assert task_func(input_string) == expected_output

def test_task_func_mixed_content():
    input_string = "Here's a link: https://www.example.com and some text, then another link: http://www.google.com"
    expected_output = {
        "www.example.com": "93.184.216.34",  # Example IP, may change
        "www.google.com": "172.217.16.196"   # Example IP, may change
    }
    assert task_func(input_string) == expected_output

def test_task_func_empty_string():
    input_string = ""
    expected_output = {}
    assert task_func(input_string) == expected_output