import pytest
from src_0380 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    # Test with a specific length
    length = 5
    result = task_func(length)
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert len(result) == length, "The DataFrame should have the specified length"
    assert set(result.columns) == set(COLUMNS), "The columns should match the expected columns"
    assert result.shape[1] == len(COLUMNS), "The number of columns should match the expected number of columns"

    # Additional tests can be added to cover more edge cases and scenarios