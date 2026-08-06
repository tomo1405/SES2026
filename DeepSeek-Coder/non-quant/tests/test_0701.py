import pytest
from src_0701 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [2, 3, 4, 5, 6]
    }
    cols = ['A', 'B', 'C']
    
    result = task_func(data, cols)
    
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert result.shape == (3, 3), "The DataFrame should have the correct shape"
    assert np.isclose(result.iloc[0, 1], -1.0), "The correlation should be -1.0"