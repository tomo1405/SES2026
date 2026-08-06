import pandas as pd
import numpy as np
import pytest
from src_0926 import task_func

def test_task_func_default_args():
    """Test the function with default arguments."""
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1000, 5)
    assert df.columns.tolist() == ['A', 'B', 'C', 'D', 'E']
    assert df.loc[0, 'A'] == -1

def test_task_func_custom_args():
    """Test the function with custom arguments."""
    df = task_func(data_size=100, column_names=['X', 'Y', 'Z'], seed=42)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (100, 3)
    assert df.columns.tolist() == ['X', 'Y', 'Z']
    assert df.loc[0, 'X'] == -1

def test_task_func_invalid_args():
    """Test the function with invalid arguments."""
    with pytest.raises(ValueError):
        task_func(data_size=-100)
    with pytest.raises(ValueError):
        task_func(column_names=['A', 'B'])