python
import pandas as pd
import matplotlib.pyplot as plt
import pytest

from src_0110 import task_func

def test_task_func():
    df = pd.DataFrame({'Item': ['apple', 'banana', 'grape', 'orange', 'pineapple'],
                       'Location': ['store1', 'store2', 'store3', 'store4', 'store5'],
                       'Quantity': [10, 20, 30, 40, 50]})

    # Test case 1: Valid input
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)

    # Test case 2: Invalid input (df is not a DataFrame)
    with pytest.raises(ValueError):
        task_func(123)

    # Test case 3: Invalid input (df does not have 'Item' and 'Location' columns)
    with pytest.raises(ValueError):
        task_func(pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}))

    # Test case 4: Invalid input (items is not a list)
    with pytest.raises(ValueError):
        task_func(df, items='apple, banana, grape, orange, pineapple')

    # Test case 5: Invalid input (locations is not a list)
    with pytest.raises(ValueError):
        task_func(df, locations='store1, store2, store3, store4, store5')

    # Test case 6: Invalid input (items and locations have different lengths)
    with pytest.raises(ValueError):
        task_func(df, items=['apple', 'banana', 'grape', 'orange'], locations=['store1', 'store2', 'store3', 'store4', 'store5', 'store6'])