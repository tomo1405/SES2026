import pytest
from src_0836 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    # Test with default parameters
    result = task_func(n_rows=5, remove_cols=[0])
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert result.shape == (5, 4), "The DataFrame should have the correct shape"

    # Add more tests as needed to cover different scenarios