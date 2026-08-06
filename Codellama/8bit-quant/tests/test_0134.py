import pytest
from src_0134 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def test_task_func_input_type():
    with pytest.raises(ValueError):
        task_func(1)

def test_task_func_input_empty_df():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_input_non_empty_df():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    normalized_df, ax = task_func(df)
    assert isinstance(normalized_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert normalized_df.equals(df)
    assert ax.get_title() == f'Normalized Data of {df.columns[-1]}'
    assert ax.get_xlabel() == 'Index'
    assert ax.get_ylabel() == 'Normalized Value'