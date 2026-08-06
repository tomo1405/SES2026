import pytest
from src_1067 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    data, outliers, _ = task_func()
    assert len(data) > 0, "Data should not be empty"
    assert len(outliers) > 0, "Outliers should be detected"

    # Add more test cases as needed

# Add more test cases as needed