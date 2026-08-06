import pytest
from src_0690 import task_func
import numpy as np
from scipy import stats
import pandas as pd

@pytest.fixture
def sample_data():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [2, 2, 2, 2, 2]
    }
    return pd.DataFrame(data)

def test_task_func(sample_data):
    result = task_func(sample_data)
    assert isinstance(result, dict), "The result should be a dictionary."
    assert len(result) == len(sample_data.columns), "The number of columns should match."
    for key in result:
        assert isinstance(result[key], float), "Each p-value should be a float."