import pytest
from src_1028 import task_func

def test_task_func_valid_hex_query():
    url = "http://example.com/?q=48656c6c6f20576f726c64"
    expected_output = "Hello World"
    assert task_func(url) == expected_output

def test_task_func_invalid_hex_query():
    url = "http://example.com/?q=invalidhex"
    assert task_func(url) is None

def test_task_func_no_query():
    url = "http://example.com/"
    assert task_func(url) is None

def test_task_func_empty_query():
    url = "http://example.com/?q="
    assert task_func(url) is None

def test_task_func_query_with_other_params():
    url = "http://example.com/?q=48656c6c6f20576f726c64&other=param"
    expected_output = "Hello World"
    assert task_func(url) == expected_output

def test_task_func_query_with_spaces():
    url = "http://example.com/?q=202020"
    expected_output = "   "
    assert task_func(url) == expected_output

def test_task_func_query_with_special_chars():
    url = "http://example.com/?q=23212a2b"
    expected_output = "#*+"
    assert task_func(url) == expected_output

def test_task_func_query_with_mixed_case():
    url = "http://example.com/?q=48656C6C6F20576F726C64"
    expected_output = "Hello World"
    assert task_func(url) == expected_output