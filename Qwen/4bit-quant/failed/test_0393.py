import pytest
from src_0393 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'Category': ['A', 'B', 'C', 'A', 'B', 'C'],
        'Value': [10, 20, 30, 40, 50, 60]
    }
    return pd.DataFrame(data)

def test_task_func_with_valid_group(sample_df):
    ax = task_func(sample_df, 'Category', 'Value', 'A')
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 2  # There should be 2 bars for group 'A'

def test_task_func_with_invalid_group(sample_df):
    with pytest.raises(ValueError):
        task_func(sample_df, 'Category', 'Value', 'D')

def test_task_func_with_empty_group(sample_df):
    with pytest.raises(ValueError):
        task_func(sample_df, 'Category', 'Value', 'Z')

def test_task_func_with_single_group(sample_df):
    ax = task_func(sample_df, 'Category', 'Value', 'B')
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 1  # There should be 1 bar for group 'B'

def test_task_func_with_multiple_groups(sample_df):
    ax = task_func(sample_df, 'Category', 'Value', 'C')
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 2  # There should be 2 bars for group 'C'