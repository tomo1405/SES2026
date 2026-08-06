import pandas as pd
import matplotlib.pyplot as plt
import pytest

from src_0110 import task_func

def test_task_func():
    # Test case 1: Invalid 'df' input
    with pytest.raises(ValueError) as exc_info:
        task_func('invalid_input', items=['apple', 'banana'], locations=['store1', 'store2'])
    assert "Invalid 'df': must be a DataFrame with 'Item' and 'Location' columns." in str(exc_info.value)

    # Test case 2: Valid 'df' input, default 'items' and 'locations'
    df = pd.DataFrame({
        'Item': ['apple', 'banana', 'grape', 'orange', 'pineapple'],
        'Location': ['store1', 'store2', 'store3', 'store4', 'store5'],
        'Quantity': [10, 20, 30, 40, 50]
    })
    ax = task_func(df)
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test case 3: Valid 'df' input, custom 'items' and 'locations'
    ax = task_func(df, items=['apple', 'banana'], locations=['store1', 'store2'])
    assert isinstance(ax, matplotlib.axes.Axes)