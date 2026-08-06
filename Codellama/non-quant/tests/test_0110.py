import matplotlib.pyplot as plt
import pandas as pd
import pytest
from src_0110 import task_func


def test_task_func_valid_input():
    df = pd.DataFrame({'Item': ['apple', 'banana', 'grape', 'orange', 'pineapple'],
                       'Location': ['store1', 'store2', 'store3', 'store4', 'store5']})
    items = ['apple', 'banana', 'grape', 'orange', 'pineapple']
    locations = ['store1', 'store2', 'store3', 'store4', 'store5']
    ax = task_func(df, items, locations)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Item Distribution by Location'
    assert ax.get_ylabel() == 'Count'

def test_task_func_invalid_input():
    df = pd.DataFrame({'Item': ['apple', 'banana', 'grape', 'orange', 'pineapple'],
                       'Location': ['store1', 'store2', 'store3', 'store4', 'store5']})
    items = ['apple', 'banana', 'grape', 'orange', 'pineapple']
    locations = ['store1', 'store2', 'store3', 'store4', 'store5']
    with pytest.raises(ValueError):
        task_func(df, items, locations, 'invalid_input')