import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from src_0293 import task_func
import pytest

def test_task_func():
    # Create a sample dataframe
    df = pd.DataFrame({
        'id': [1, 1, 2, 2, 3, 3],
        'age': [25, 30, 28, 32, 27, 35],
        'income': [50000, 60000, 55000, 65000, 45000, 70000]
    })

    # Call the function
    df_grouped, (hist, bins) = task_func(df)

    # Check the output type
    assert isinstance(df_grouped, pd.DataFrame)
    assert isinstance(hist, np.ndarray)
    assert isinstance(bins, np.ndarray)

    # Check the content of the output
    assert df_grouped.shape == (6, 3)
    assert hist.shape == (10,)
    assert bins.shape == (11,)
    assert np.all(hist >= 0)
    assert np.all(bins[:-1] < bins[1:])

def test_task_func_with_nan():
    # Create a sample dataframe with NaN values
    df = pd.DataFrame({
        'id': [1, 1, 2, 2, 3, 3],
        'age': [25, 30, 28, np.nan, 27, 35],
        'income': [50000, 60000, 55000, 65000, np.nan, 70000]
    })

    # Call the function
    df_grouped, (hist, bins) = task_func(df)

    # Check the output type
    assert isinstance(df_grouped, pd.DataFrame)
    assert isinstance(hist, np.ndarray)
    assert isinstance(bins, np.ndarray)

    # Check the content of the output
    assert df_grouped.shape == (6, 3)
    assert hist.shape == (10,)
    assert bins.shape == (11,)
    assert np.all(hist >= 0)
    assert np.all(bins[:-1] < bins[1:])