import pytest
from src_0111 import task_func
import pandas as pd

def test_task_func_valid_input():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Sales': [10, 20, 30]})
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)

def test_task_func_invalid_input():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Sales': [10, 20, 30]})
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_empty_input():
    df = pd.DataFrame({'Date': [], 'Sales': []})
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_no_data_available():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Sales': [0, 0, 0]})
    with pytest.raises(ValueError):
        task_func(df)