import matplotlib.pyplot as plt
import pandas as pd
import pytest
from src_0134 import task_func


def test_task_func():
    # Test 1: Input is not a DataFrame
    with pytest.raises(ValueError):
        task_func(1)

    # Test 2: Input is an empty DataFrame
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())

    # Test 3: Input is a valid DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    normalized_df, ax = task_func(df)
    assert isinstance(normalized_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert normalized_df.equals(df)
    assert ax.get_title() == f'Normalized Data of {df.columns[-1]}'
    assert ax.get_xlabel() == 'Index'
    assert ax.get_ylabel() == 'Normalized Value'