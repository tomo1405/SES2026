import pytest
from src_0534 import task_func

def test_task_func():
    # Test case 1: Basic conversion
    assert task_func(123, 10, 16, "0123456789ABCDEF") == ('B3V', 'salt')

    # Add more test cases as needed