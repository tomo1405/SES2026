import pytest
from src_1120 import task_func

def test_task_func():
    # Test case 1: Default password length and salt
    result = task_func()
    assert len(result) == 10  # Assuming default password length is 10

    # Add more test cases as needed