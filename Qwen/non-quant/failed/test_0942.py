import pytest
from src_0942 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def expected_data():
    start_date = '2023-01-01'
    periods = 5
    freq = 'D'
    random_seed = 0
    np.random.seed(random_seed)
    date_range = pd.date_range(start_date, periods=periods, freq=freq)
    sales_forecast = np.random.randint(100, 500, size=periods)
    expected_df = pd.DataFrame({'Date': date_range, 'Sales': sales_forecast}).set_index('Date')
    return expected_df

def test_task_func_output(expected_data):
    start_date = '2023-01-01'
    periods = 5
    freq = 'D'
    random_seed = 0
    forecast_df, ax = task_func(start_date, periods, freq, random_seed)
    
    # Check if the DataFrame is correct
    pd.testing.assert_frame_equal(forecast_df, expected_data)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Sales Forecast'
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Sales'
    assert ax.gridOn

def test_task_func_with_different_seed():
    start_date = '2023-01-01'
    periods = 5
    freq = 'D'
    random_seed = 1
    forecast_df, ax = task_func(start_date, periods, freq, random_seed)
    
    # Check if the DataFrame is not empty and has the correct shape
    assert not forecast_df.empty
    assert forecast_df.shape == (periods, 1)

def test_task_func_with_invalid_start_date():
    with pytest.raises(ValueError):
        task_func('invalid-date', 5, 'D')

def test_task_func_with_invalid_freq():
    with pytest.raises(ValueError):
        task_func('2023-01-01', 5, 'INVALID_FREQ')