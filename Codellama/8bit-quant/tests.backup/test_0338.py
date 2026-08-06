import pytest
from src_0338 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Create a sample dataframe
    df = pd.DataFrame({'group': ['A', 'B', 'C', 'A', 'B', 'C'],
                      'value': [1, 2, 3, 4, 5, 6]})

    # Test the function with a single group
    group_col = 'group'
    value_col = 'value'
    ax = task_func(df, group_col, value_col)
    assert ax.get_xlabel() == group_col
    assert ax.get_ylabel() == value_col
    assert ax.get_title() == f'Bar chart of {value_col} by {group_col}'
    assert len(ax.get_xticks()) == 3
    assert len(ax.get_yticks()) == 3
    assert ax.get_xticklabels() == ['A', 'B', 'C']
    assert ax.get_yticklabels() == ['1', '2', '3']
    assert ax.get_legend().get_texts() == ['Group 1', 'Group 2', 'Group 3']

    # Test the function with multiple groups
    group_col = 'group'
    value_col = 'value'
    ax = task_func(df, group_col, value_col)
    assert ax.get_xlabel() == group_col
    assert ax.get_ylabel() == value_col
    assert ax.get_title() == f'Bar chart of {value_col} by {group_col}'
    assert len(ax.get_xticks()) == 3
    assert len(ax.get_yticks()) == 3
    assert ax.get_xticklabels() == ['A', 'B', 'C']
    assert ax.get_yticklabels() == ['1', '2', '3']
    assert ax.get_legend().get_texts() == ['Group 1', 'Group 2', 'Group 3']

    # Test the function with a different value column
    group_col = 'group'
    value_col = 'value2'
    ax = task_func(df, group_col, value_col)
    assert ax.get_xlabel() == group_col
    assert ax.get_ylabel() == value_col
    assert ax.get_title() == f'Bar chart of {value_col} by {group_col}'
    assert len(ax.get_xticks()) == 3
    assert len(ax.get_yticks()) == 3
    assert ax.get_xticklabels() == ['A', 'B', 'C']
    assert ax.get_yticklabels() == ['1', '2', '3']
    assert ax.get_legend().get_texts() == ['Group 1', 'Group 2', 'Group 3']