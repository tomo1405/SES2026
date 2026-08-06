import pytest
from src_0434 import task_func

def test_task_func():
    # Test case 1: Valid input
    assert task_func("dGVzdA==", "7f83b16a1639e56e3e6e6c1add8a9b5b5d4a7c7d1", "secret") == True

    # Add more test cases as needed