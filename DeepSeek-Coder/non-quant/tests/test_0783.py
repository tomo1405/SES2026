import pytest
from src_0783 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    result = task_func(n=5)
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert len(result) == 5, "The DataFrame should have 5 rows"

    # Add more test cases as needed