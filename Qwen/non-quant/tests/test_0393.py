import pytest
from src_0393 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'category': ['A', 'A', 'B', 'B', 'C'],
        'value': [10, 20, 30, 40, 50]
    }
    return pd.DataFrame(data)

def test_task_func_with_valid_group(sample_df):
    ax = task_func(sample_df, 'category', 'value', 'A')
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 2
    assert ax.get_title() == 'Bar chart of value for A'
    assert ax.get_xlabel() == 'category'
    assert ax.get_ylabel() == 'value'

def test_task_func_with_invalid_group(sample_df):
    with pytest.raises(ValueError):
        task_func(sample_df, 'category', 'value', 'D')

def test_task_func_with_single_bar(sample_df):
    ax = task_func(sample_df, 'category', 'value', 'C')
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 1
    assert ax.get_title() == 'Bar chart of value for C'
    assert ax.get_xlabel() == 'category'
    assert ax.get_ylabel() == 'value'

def test_task_func_with_multiple_groups(sample_df):
    ax = task_func(sample_df, 'category', 'value', 'B')
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 2
    assert ax.get_title() == 'Bar chart of value for B'
    assert ax.get_xlabel() == 'category'
    assert ax.get_ylabel() == 'value'