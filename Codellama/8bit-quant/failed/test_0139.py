import pytest
from src_0139 import task_func
import pandas as pd

def test_task_func_valid_input():
    df = pd.DataFrame({'Letters': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']})
    ax = task_func(df)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_title() == 'Letter Frequency'
    assert ax.get_xlabel() == 'Letters'
    assert ax.get_ylabel() == 'Frequency'

def test_task_func_invalid_input():
    df = pd.DataFrame({'Numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    with pytest.raises(ValueError):
        task_func(df)