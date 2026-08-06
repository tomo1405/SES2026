import pytest
from src_0111 import task_func
import pandas as pd

def test_task_func_valid_input():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Sales': [10, 20, 30]})
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Daily Turnover'
    assert ax.get_ylabel() == 'Sales'

def test_task_func_invalid_input():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Sales': [10, 20, 30]})
    with pytest.raises(ValueError):
        task_func(df)