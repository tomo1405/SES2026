import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import pytest


def task_func(df, items=None, locations=None):
    if not isinstance(df, pd.DataFrame) or not all(col in df.columns for col in ['Item', 'Location']):
        raise ValueError("Invalid 'df': must be a DataFrame with 'Item' and 'Location' columns.")

    items = items or ['apple', 'banana', 'grape', 'orange', 'pineapple']
    locations = locations or ['store1', 'store2', 'store3', 'store4', 'store5']

    item_count_df = df.groupby(['Location', 'Item']).size().unstack().fillna(0)
    ax = item_count_df.plot(kind='bar', stacked=True)
    ax.set_title('Item Distribution by Location')
    ax.set_ylabel('Count')
    plt.show()
    return ax

def test_task_func():
    # Test case 1: Invalid 'df'
    with pytest.raises(ValueError):
        task_func('not_a_dataframe')

    # Test case 2: Valid 'df' with 'Item' and 'Location' columns
    df = pd.DataFrame({
        'Item': ['apple', 'banana', 'grape', 'orange', 'pineapple'],
        'Location': ['store1', 'store2', 'store3', 'store4', 'store5']
    })
    ax = task_func(df)
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test case 3: Valid 'df' with 'Item' and 'Location' columns, custom 'items' and 'locations'
    df = pd.DataFrame({
        'Item': ['apple', 'banana', 'grape', 'orange', 'pineapple', 'apple', 'banana', 'grape', 'orange', 'pineapple'],
        'Location': ['store1', 'store2', 'store3', 'store4', 'store5', 'store1', 'store2', 'store3', 'store4', 'store5']
    })
    ax = task_func(df, items=['apple', 'banana'], locations=['store1', 'store2'])
    assert isinstance(ax, matplotlib.axes.Axes)