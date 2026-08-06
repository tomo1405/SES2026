import pytest
from src_0870 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    result = task_func(n_grades=5, rng_seed=42)
    assert len(result) == 5
    assert all(col in result.columns for col in ['Student', 'Grade'])

    # Add more test cases as needed

# Add more test cases as needed