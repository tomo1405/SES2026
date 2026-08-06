import pytest
from src_0942 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    start_date = '2022-01-01'
    periods = 10
    freq = 'D'
    random_seed = 0
    forecast_df, ax = task_func(start_date, periods, freq, random_seed)

    assert isinstance(forecast_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert len(forecast_df) == periods
    assert forecast_df.index.freq == freq
    assert forecast_df['Sales'].dtype == np.int64
    assert forecast_df['Sales'].min() >= 100
    assert forecast_df['Sales'].max() <= 500
    assert ax.get_title() == 'Sales Forecast'
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Sales'
    assert ax.get_grid()