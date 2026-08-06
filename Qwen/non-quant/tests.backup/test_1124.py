import pytest
from src_1124 import task_func

def test_task_func_no_urls():
    input_string = "This is a test string without any URLs."
    expected_output = {}
    assert task_func(input_string) == expected_output

def test_task_func_single_url():
    input_string = "Check out this website: https://example.com"
    # Note: The actual SSL expiry date will vary, so we cannot assert an exact value.
    # We can check that the domain is in the output dictionary.
    result = task_func(input_string)
    assert 'example.com' in result

def test_task_func_multiple_urls():
    input_string = "Visit these sites: https://example.com, https://test.com"
    result = task_func(input_string)
    assert 'example.com' in result
    assert 'test.com' in result

def test_task_func_invalid_url():
    input_string = "Invalid URL here: https://invalid-url"
    result = task_func(input_string)
    # Assuming the invalid URL will raise an SSL error and be ignored
    assert 'invalid-url' not in result

def test_task_func_no_ssl_support():
    input_string = "This site does not support SSL: http://example.com"
    expected_output = {}
    assert task_func(input_string) == expected_output

# This test assumes that the network is reachable and the SSL certificates are valid.
def test_task_func_real_url():
    input_string = "Check out this website: https://www.google.com"
    result = task_func(input_string)
    assert 'www.google.com' in result