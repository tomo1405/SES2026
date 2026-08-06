import pytest
from src_0393 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: Test with valid input
    df = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': [1, 2, 3]})
    group_col = 'A'
    value_col = 'B'
    group_name = 'a'
    ax = task_func(df, group_col, value_col, group_name)
    assert ax.get_xlabel() == 'A'
    assert ax.get_ylabel() == 'B'
    assert ax.get_title() == 'Bar chart of B for a'
    assert ax.get_xticks() == np.arange(len(df[df[group_col] == group_name]))
    assert ax.get_xticklabels() == df[df[group_col] == group_name][group_col]
    assert ax.get_bar_width() == 0.35
    assert ax.get_color() == COLORS[:len(df[df[group_col] == group_name])]

    # Test case 2: Test with invalid input
    df = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': [1, 2, 3]})
    group_col = 'A'
    value_col = 'B'
    group_name = 'd'
    with pytest.raises(ValueError):
        task_func(df, group_col, value_col, group_name)