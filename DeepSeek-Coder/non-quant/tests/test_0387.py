import pytest
from src_0387 import task_func

def test_task_func():
    # Test the function with default parameters
    result = task_func(10)
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert len(result) == 10, "The DataFrame should have 10 rows"

    # Add more test cases as needed