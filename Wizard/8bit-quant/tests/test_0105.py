python
import pandas as pd
import matplotlib.pyplot as plt
from itertools import cycle
import pytest

def task_func(df, groups=['A', 'B', 'C', 'D', 'E']):

    if not isinstance(df, pd.DataFrame) or not all(col in df.columns for col in ['group', 'date', 'value']):
        raise ValueError("Invalid 'df': must be a DataFrame with 'group', 'date', and 'value' columns.")

    color_cycle = cycle('bgrcmk')
    fig, ax = plt.subplots(figsize=(10, 6))

    for group in groups:
        group_df = df[df['group'] == group].copy()
        group_df['date'] = group_df['date'].apply(lambda x: x.toordinal())
        ax.scatter(group_df['date'], group_df['value'], color=next(color_cycle))

    ax.set_xlabel('Date (ordinal)')
    ax.set_ylabel('Value')
    ax.set_title('Scatterplot of Values for Each Group Over Time')

    return ax

def test_task_func():
    df = pd.DataFrame({'group': ['A', 'B', 'C', 'D', 'E'],
                       'date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05'],
                       'value': [1, 2, 3, 4, 5]})

    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'Date (ordinal)'
    assert ax.get_ylabel() == 'Value'
    assert ax.get_title() == 'Scatterplot of Values for Each Group Over Time'