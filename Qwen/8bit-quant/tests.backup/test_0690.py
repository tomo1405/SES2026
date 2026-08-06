import pytest
from src_0690 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_df():
    data = {
        'A': np.random.normal(loc=0, scale=1, size=100),
        'B': np.random.exponential(scale=1/1, size=100),
        'C': np.random.uniform(low=0, high=1, size=100)
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    p_values = task_func(sample_df)
    
    # Check that the result is a dictionary
    assert isinstance(p_values, dict)
    
    # Check that each column has a p-value
    for col in sample_df.columns:
        assert col in p_values
        assert isinstance(p_values[col], float)
    
    # Check that p-values are within the valid range [0, 1]
    for p_value in p_values.values():
        assert 0 <= p_value <= 1

def test_task_func_empty_df():
    empty_df = pd.DataFrame()
    p_values = task_func(empty_df)
    
    # Check that the result is an empty dictionary
    assert p_values == {}