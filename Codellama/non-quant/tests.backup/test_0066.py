import pytest
from src_0066 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    data = [
        {'col1': 'A', 'col2': 'B', 'col3': 'C'},
        {'col1': 'A', 'col2': 'B', 'col3': 'D'},
        {'col1': 'A', 'col2': 'C', 'col3': 'D'},
        {'col1': 'B', 'col2': 'C', 'col3': 'D'},
        {'col1': 'B', 'col2': 'C', 'col3': 'E'},
        {'col1': 'B', 'col2': 'D', 'col3': 'E'},
        {'col1': 'C', 'col2': 'D', 'col3': 'E'},
        {'col1': 'C', 'col2': 'D', 'col3': 'F'},
        {'col1': 'C', 'col2': 'E', 'col3': 'F'},
        {'col1': 'D', 'col2': 'E', 'col3': 'F'},
    ]
    expected_analyzed_df = pd.DataFrame(
        {'col1': ['A', 'B', 'C', 'D', 'E'],
         'col2': ['B', 'C', 'D', 'E', 'F'],
         'col3': [2, 3, 2, 2, 1]
        })
    expected_ax = plt.subplots()
    expected_ax.plot(expected_analyzed_df[['col1', 'col2']].astype(str).agg('-'.join, axis=1), expected_analyzed_df['col3'])
    expected_ax.set_xlabel('-'.join(['col1', 'col2']))
    expected_ax.set_ylabel('col3')

    analyzed_df, ax = task_func(data)

    assert analyzed_df.equals(expected_analyzed_df)
    assert ax.get_xlabel() == expected_ax.get_xlabel()
    assert ax.get_ylabel() == expected_ax.get_ylabel()
    assert ax.get_title() == expected_ax.get_title()
    assert ax.get_xlim() == expected_ax.get_xlim()
    assert ax.get_ylim() == expected_ax.get_ylim()
    assert ax.get_xticks() == expected_ax.get_xticks()
    assert ax.get_yticks() == expected_ax.get_yticks()
    assert ax.get_xticklabels() == expected_ax.get_xticklabels()
    assert ax.get_yticklabels() == expected_ax.get_yticklabels()
    assert ax.get_xaxis().get_major_formatter().format_data(ax.get_xaxis().get_major_locator().locator_params) == expected_ax.get_xaxis().get_major_formatter().format_data(expected_ax.get_xaxis().get_major_locator().locator_params)
    assert ax.get_yaxis().get_major_formatter().format_data(ax.get_yaxis().get_major_locator().locator_params) == expected_ax.get_yaxis().get_major_formatter().format_data(expected_ax.get_yaxis().get_major_locator().locator_params)