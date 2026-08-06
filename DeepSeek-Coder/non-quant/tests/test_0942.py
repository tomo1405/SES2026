import pytest
from src_0942 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    start_date = '2023-01-01'
    periods = 10
    freq = 'D'
    random_seed = 42

    result = task_func(start_date=start_date, periods=periods, freq=freq, random_seed=random_seed)

    assert isinstance(result, tuple), "The function should return a tuple."
    assert len(result) == 2, "The function should return a tuple with two elements."
    assert isinstance(result[0], pd.DataFrame), "The first element should be a DataFrame."
    assert isinstance(result[1], plt.Axes), "The second element should be a matplotlib Axes object."

    df = result[0]
    assert isinstance(df, pd.DataFrame), "The first element should be a DataFrame."
    assert not df.empty, "The DataFrame should not be empty."
    assert 'Date' in df.columns, "The DataFrame should have a 'Date' column."
    assert 'Sales' in df.columns, "The DataFrame should have a 'Sales' column."

    ax = result[1]
    assert isinstance(ax, plt.Axes), "The second element should be a matplotlib Axes object."
    assert ax.get_title() == 'Sales Forecast', "The plot should have the correct title."
    assert ax.get_xlabel() == 'Date', "The x-axis label should be 'Date'."
    assert ax.get_ylabel() == 'Sales', "The y-axis label should be 'Sales'."
    assert ax.get_grid(), "The plot should have a grid."