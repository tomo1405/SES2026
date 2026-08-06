import pytest
from src_0976 import task_func

def test_task_func():
    # Test case 1: Default parameters
    result = task_func(rows=5)
    assert result.shape == (5, 5)
    assert set(result.columns) == {'A', 'B', 'C', 'D', 'E'}

    # Add more test cases as needed