import pytest
from src_1028 import task_func

def test_task_func_valid_hex_query():
    url = "http://example.com?q=48656c6c6f20576f726c64"
    assert task_func(url) == "Hello World"

def test_task_func_invalid_hex_query():
    url = "http://example.com?q=ZZZ"
    assert task_func(url) is None

def test_task_func_no_query():
    url = "http://example.com"
    assert task_func(url) is None

def test_task_func_empty_query():
    url = "http://example.com?q="
    assert task_func(url) is None

def test_task_func_non_ascii_query():
    url = "http://example.com?q=48656c6c6f20576f726c64e298ba"
    assert task_func(url) == "Hello World😊"

def test_task_func_unicode_decode_error():
    url = "http://example.com?q=48656c6c6f20576f726c64\x80"
    assert task_func(url) is None

def test_task_func_binascii_error():
    url = "http://example.com?q=48656c6c6f20576f726c64G"
    assert task_func(url) is None