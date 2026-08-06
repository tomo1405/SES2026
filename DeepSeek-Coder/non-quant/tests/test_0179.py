import pytest
from src_0179 import task_func

def test_valid_ip():
    assert task_func("192.168.1.1") == "Invalid IP address received"

def test_invalid_ip():
    assert task_func("256.256.256.256") == "Invalid IP address received"

def test_exception():
    assert task_func("invalid ip") == "Invalid IP address received"