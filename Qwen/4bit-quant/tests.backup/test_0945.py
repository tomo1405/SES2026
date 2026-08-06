import pytest
from src_0945 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_default():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert 'Date' in df.index.name
    assert 'Price' in df.columns
    assert len(df) == 13
    assert isinstance(ax, plt.Axes)

def test_task_func_custom_dates():
    start_date = '2020-01-01'
    periods = 5
    freq = 'D'
    df, ax = task_func(start_date=start_date, periods=periods, freq=freq)
    assert df.index[0] == pd.to_datetime(start_date)
    assert len(df) == periods

def test_task_func_random_seed():
    seed = 42
    df1, _ = task_func(seed=seed)
    df2, _ = task_func(seed=seed)
    assert df1.equals(df2)

def test_task_func_no_plot():
    df, ax = task_func()
    assert ax.figure is not None
    plt.close(ax.figure)

def test_task_func_invalid_freq():
    with pytest.raises(ValueError):
        task_func(freq='INVALID_FREQ')

def test_task_func_negative_periods():
    with pytest.raises(ValueError):
        task_func(periods=-5)