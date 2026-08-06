import pytest
from src_0105 import task_func
import pandas as pd

def test_task_func_invalid_df():
    with pytest.raises(ValueError):
        task_func(None)

def test_task_func_missing_columns():
    df = pd.DataFrame({
        'group': ['A', 'B'],
        'date': ['2021-01-01', '2021-01-02']
    })
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_valid_input():
    df = pd.DataFrame({
        'group': ['A', 'A', 'B', 'B'],
        'date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04'],
        'value': [10, 20, 30, 40]
    })
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_custom_groups():
    df = pd.DataFrame({
        'group': ['X', 'X', 'Y', 'Y'],
        'date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04'],
        'value': [10, 20, 30, 40]
    })
    ax = task_func(df, groups=['X', 'Y'])
    assert isinstance(ax, plt.Axes)