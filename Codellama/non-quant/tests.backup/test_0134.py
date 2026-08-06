import pytest
from src_0134 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def test_task_func():
    # Test case 1: Input is a non-empty DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    normalized_df, ax = task_func(df)
    assert isinstance(normalized_df, pd.DataFrame)
    assert not normalized_df.empty
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == f'Normalized Data of {df.columns[-1]}'
    assert ax.get_xlabel() == 'Index'
    assert ax.get_ylabel() == 'Normalized Value'

    # Test case 2: Input is an empty DataFrame
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)

    # Test case 3: Input is not a DataFrame
    df = [1, 2, 3]
    with pytest.raises(ValueError):
        task_func(df)