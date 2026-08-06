import pytest
from src_0668 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    assert task_func([1, 1, 2, 2, 3], 2) == [1, 2]
    
    # Add more test cases as needed