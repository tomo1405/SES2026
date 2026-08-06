import pytest
from src_0342 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def numeric_df():
    return pd.DataFrame({
        'A': np.random.randn(100),
        'B': np.random.randint(0, 100, 100)
    })

@pytest.fixture
def categorical_df():
    return pd.DataFrame({
        'C': ['foo', 'bar', 'baz'] * 33 + ['qux'],
        'D': ['alpha', 'beta', 'gamma'] * 34
    })

def test_task_func_numeric_column(numeric_df):
    fig = task_func(numeric_df, 'A')
    assert isinstance(fig, plt.Figure)
    plt.close(fig)

def test_task_func_categorical_column(categorical_df):
    fig = task_func(categorical_df, 'C')
    assert isinstance(fig, plt.Figure)
    plt.close(fig)

def test_task_func_invalid_dataframe():
    with pytest.raises(ValueError):
        task_func(None, 'A')

def test_task_func_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df, 'A')

def test_task_func_nonexistent_column(numeric_df):
    with pytest.raises(ValueError):
        task_func(numeric_df, 'Z')