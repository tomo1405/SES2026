import pytest
from src_0838 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    result = task_func(n_rows=10, scale_cols=[0], random_seed=42)
    assert result is not None

    # Add more test cases as needed