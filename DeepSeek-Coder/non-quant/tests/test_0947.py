import pytest
from src_0947 import task_func

def test_task_func():
    # Test with default parameters
    result = task_func()
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert result.shape == (3, 2), "The DataFrame should have 3 rows and 2 columns"

    # Test with custom parameters
    result = task_func(rows=5, cols=4, min_val=10, max_val=50, seed=42)
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert result.shape == (5, 4), "The DataFrame should have 5 rows and 4 columns"

    # Test with min_val equal to max_val
    result = task_func(min_val=100, max_val=100)
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert result.shape == (3, 2), "The DataFrame should have 3 rows and 2 columns"