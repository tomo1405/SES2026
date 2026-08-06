import pytest
from src_0981 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': ['a', 'b', 'c']
    }
    return pd.DataFrame(data)

def test_task_func_with_numeric_data(sample_df):
    df, fig = task_func(sample_df)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(fig, plt.Figure)
    assert all(df.dtypes == float)  # Check if all numeric columns are scaled

def test_task_func_with_no_numeric_data():
    data = {'C': ['a', 'b', 'c']}
    df = pd.DataFrame(data)
    with pytest.raises(ValueError, match="No numeric columns present"):
        task_func(df)

def test_task_func_with_empty_df():
    df = pd.DataFrame()
    with pytest.raises(ValueError, match="No numeric columns present"):
        task_func(df)