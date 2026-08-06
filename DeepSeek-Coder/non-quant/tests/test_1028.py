import pytest
from src_1028 import task_func

def test_task_func_valid_url():
    assert task_func("http://example.com?q=41514151") == "test"

def test_task_func_invalid_url():
    assert task_func("http://example.com") is None