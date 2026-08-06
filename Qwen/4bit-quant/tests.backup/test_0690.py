import pytest
from src_0690 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_df():
    data = {
        'A': np.random.normal(loc=0, scale=1, size=100),
        'B': np.random.normal(loc=1, scale=2, size=100),
        'C': np.random.exponential(scale=1.0, size=100)
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    p_values = task_func(sample_df)
    
    # Check that the number of keys in p_values matches the number of columns in the DataFrame
    assert len(p_values) == len(sample_df.columns)
    
    # Check that each key in p_values is a column name from the DataFrame
    assert all(col in p_values for col in sample_df.columns)
    
    # Check that each p-value is a float between 0 and 1
    for p_value in p_values.values():
        assert isinstance(p_value, float)
        assert 0 <= p_value <= 1

def test_task_func_empty_df():
    empty_df = pd.DataFrame()
    p_values = task_func(empty_df)
    
    # Check that p_values is an empty dictionary
    assert p_values == {}

def test_task_func_single_column_df():
    data = {'A': np.random.normal(loc=0, scale=1, size=100)}
    single_column_df = pd.DataFrame(data)
    p_values = task_func(single_column_df)
    
    # Check that p_values contains only one key
    assert len(p_values) == 1
    
    # Check that the key in p_values is 'A'
    assert 'A' in p_values
    
    # Check that the p-value is a float between 0 and 1
    assert isinstance(p_values['A'], float)
    assert 0 <= p_values['A'] <= 1