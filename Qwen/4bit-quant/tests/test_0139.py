import matplotlib.pyplot as plt
import pandas as pd
import pytest
from src_0139 import task_func


def test_task_func_with_valid_data():
    data = {'Letters': ['A', 'B', 'A', 'C', 'B', 'A']}
    df = pd.DataFrame(data)
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_missing_letters_column():
    data = {'Numbers': [1, 2, 3]}
    df = pd.DataFrame(data)
    with pytest.raises(ValueError, match="The input must be a pandas DataFrame with a 'Letters' column."):
        task_func(df)

def test_task_func_with_non_dataframe_input():
    with pytest.raises(ValueError, match="The input must be a pandas DataFrame with a 'Letters' column."):
        task_func([1, 2, 3])

def test_task_func_with_custom_letters():
    data = {'Letters': ['X', 'Y', 'Z', 'X', 'Y']}
    df = pd.DataFrame(data)
    custom_letters = list('XYZ')
    ax = task_func(df, custom_letters)
    assert isinstance(ax, plt.Axes)