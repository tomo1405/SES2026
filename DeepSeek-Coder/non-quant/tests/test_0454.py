import pytest
from src_0454 import task_func

def test_task_func():
    # Test case 1: Basic test
    result = task_func(5, r'^[a-zA-Z]{5}$')
    assert result == 'ABCDE' or result == 'abcde'

    # Add more test cases as needed