python
import pandas as pd
import matplotlib.pyplot as plt
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
    # Test case 1: Valid input
    df = pd.DataFrame({'Item': ['apple', 'banana', 'grape', 'orange', 'pineapple'],
                       'Location': ['store1', 'store2', 'store3', 'store4', 'store5'],
                       'Quantity': [10, 20, 30, 40, 50]})
    items = ['apple', 'banana', 'grape', 'orange', 'pineapple']
    locations = ['store1', 'store2', 'store3', 'store4', 'store5']
    ax = task_func(df, items, locations)
    assert isinstance(ax, plt.Axes)

    # Test case 2: Invalid input (missing 'Quantity' column)
    df = pd.DataFrame({'Item': ['apple', 'banana', 'grape', 'orange', 'pineapple'],
                       'Location': ['store1', 'store2', 'store3', 'store4', 'store5']})
    items = ['apple', 'banana', 'grape', 'orange', 'pineapple']
    locations = ['store1', 'store2', 'store3', 'store4', 'store5']
    with pytest.raises(ValueError):
        task_func(df, items, locations)

    # Test case 3: Invalid input (invalid DataFrame)
    df = 'not a DataFrame'
    items = ['apple', 'banana', 'grape', 'orange', 'pineapple']
    locations = ['store1', 'store2', 'store3', 'store4', 'store5']
    with pytest.raises(ValueError):
        task_func(df, items, locations)