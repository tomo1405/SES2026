import pytest
from src_0096 import task_func

def test_task_func():
    # Test case 1: Default categories and months
    result = task_func()
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert len(result) > 0, "The DataFrame should not be empty"

    # Add more test cases as needed

# Add more test cases as needed