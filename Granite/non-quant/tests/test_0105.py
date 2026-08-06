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
    # Test case 1: Invalid 'df' (not a DataFrame)
    with pytest.raises(ValueError) as exc_info:
        task_func('not_a_dataframe')
    assert "Invalid 'df': must be a DataFrame with 'group', 'date', and 'value' columns." in str(exc_info.value)

    # Test case 2: Invalid 'df' (missing columns)
    df = pd.DataFrame({'group': ['A', 'B'], 'date': [1, 2], 'value': [3, 4]})
    with pytest.raises(ValueError) as exc_info:
        task_func(df)
    assert "Invalid 'df': must be a DataFrame with 'group', 'date', and 'value' columns." in str(exc_info.value)

    # Test case 3: Valid 'df'
    df = pd.DataFrame({'group': ['A', 'B', 'A', 'B'], 'date': [1, 2, 3, 4], 'value': [5, 6, 7, 8]})
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'Date (ordinal)'
    assert ax.get_ylabel() == 'Value'
    assert ax.get_title() == 'Scatterplot of Values for Each Group Over Time'