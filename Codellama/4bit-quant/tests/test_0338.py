from operator import index

import pandas as pd
from src_0338 import task_func


def test_task_func():
    # Test with a sample dataframe
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    group_col = 'A'
    value_col = 'B'
    ax = task_func(df, group_col, value_col)

    # Check that the bar chart is created correctly
    assert ax.get_xlabel() == group_col
    assert ax.get_ylabel() == value_col
    assert ax.get_title() == f'Bar chart of {value_col} by {group_col}'
    assert len(ax.get_xticks()) == len(df[group_col].unique())
    assert len(ax.get_yticks()) == len(df[value_col].unique())

    # Check that the error bars are created correctly
    for i, (mean, std) in enumerate(zip(df.groupby(group_col)[value_col].mean(), df.groupby(group_col)[value_col].std())):
        assert ax.get_bar(index[i], mean, yerr=std, color=COLORS[i % len(COLORS)], capsize=4, label=f'Group {i+1}')

    # Check that the legend is created correctly
    assert ax.get_legend() == f'Group {i+1}'

    # Check that the axes object is returned correctly
    assert ax == plt.gca()