import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pytest
from src_0140 import task_func

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'A': np.random.normal(size=100),
        'B': np.random.randint(0, 100, size=100),
        'C': np.random.choice(['X', 'Y', 'Z'], size=100)
    })

def test_input_type(sample_df):
    with pytest.raises(ValueError) as excinfo:
        task_func(sample_df.values)
    assert "The input must be a non-empty pandas DataFrame." in str(excinfo.value)

def test_empty_input(sample_df):
    with pytest.raises(ValueError) as excinfo:
        task_func(pd.DataFrame())
    assert "The input must be a non-empty pandas DataFrame." in str(excinfo.value)

def test_numeric_columns(sample_df):
    with pytest.raises(ValueError) as excinfo:
        task_func(sample_df[['A', 'C']])
    assert "DataFrame contains no numeric columns." in str(excinfo.value)

def test_return_value(sample_df):
    axes = task_func(sample_df[['A', 'B']])
    assert isinstance(axes, list)
    assert all(isinstance(ax, plt.Axes) for ax in axes)