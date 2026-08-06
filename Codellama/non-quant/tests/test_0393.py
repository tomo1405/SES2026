import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
from src_0393 import task_func


def test_task_func():
    # Test case 1: Empty DataFrame
    df = pd.DataFrame()
    group_col = 'group'
    value_col = 'value'
    group_name = 'A'
    with pytest.raises(ValueError):
        task_func(df, group_col, value_col, group_name)

    # Test case 2: Non-empty DataFrame, but no group with the specified name
    df = pd.DataFrame({'group': ['A', 'B', 'C'], 'value': [1, 2, 3]})
    group_col = 'group'
    value_col = 'value'
    group_name = 'D'
    with pytest.raises(ValueError):
        task_func(df, group_col, value_col, group_name)

    # Test case 3: Non-empty DataFrame, group with the specified name exists
    df = pd.DataFrame({'group': ['A', 'B', 'C'], 'value': [1, 2, 3]})
    group_col = 'group'
    value_col = 'value'
    group_name = 'A'
    ax = task_func(df, group_col, value_col, group_name)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == group_col
    assert ax.get_ylabel() == value_col
    assert ax.get_title() == f'Bar chart of {value_col} for {group_name}'
    assert len(ax.get_xticks()) == len(df)
    assert len(ax.get_xticklabels()) == len(df)
    assert all(ax.get_xticklabels() == df[group_col])
    assert all(ax.get_xticks() == np.arange(len(df)))
    assert all(ax.get_yticks() == df[value_col])
    assert all(ax.get_yticklabels() == df[value_col])