import pytest
from src_0346 import task_func
import pandas as pd
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [2, 3, 5, 7, 11]
    })

def test_task_func_with_valid_data(sample_df):
    ax = task_func(sample_df, 'x', 'y')
    assert isinstance(ax, plt.Axes)
    plt.close()

def test_task_func_with_non_dataframe():
    with pytest.raises(ValueError, match="The DataFrame is empty or the specified column does not exist."):
        task_func([1, 2, 3], 'x', 'y')

def test_task_func_with_empty_dataframe():
    with pytest.raises(ValueError, match="The DataFrame is empty or the specified column does not exist."):
        task_func(pd.DataFrame(), 'x', 'y')

def test_task_func_with_missing_column(sample_df):
    with pytest.raises(ValueError, match="The DataFrame is empty or the specified column does not exist."):
        task_func(sample_df, 'z', 'y')

def test_task_func_with_missing_columns(sample_df):
    with pytest.raises(ValueError, match="The DataFrame is empty or the specified column does not exist."):
        task_func(sample_df, 'x', 'z')