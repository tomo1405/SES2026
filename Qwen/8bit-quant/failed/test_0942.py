import pytest
from src_0942 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_output():
    start_date = '2023-01-01'
    periods = 10
    freq = 'D'
    random_seed = 42
    
    forecast_df, ax = task_func(start_date, periods, freq, random_seed)
    
    # Check if the DataFrame is correctly structured
    assert isinstance(forecast_df, pd.DataFrame)
    assert 'Sales' in forecast_df.columns
    assert len(forecast_df) == periods
    
    # Check if the DataFrame values are within the expected range
    assert (forecast_df['Sales'] >= 100).all() and (forecast_df['Sales'] <= 500).all()
    
    # Check if the plot is correctly created
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Sales Forecast'
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Sales'
    assert ax.gridOn
    
    # Check if the plot data matches the DataFrame
    plotted_data = ax.lines[0].get_ydata()
    assert np.array_equal(plotted_data, forecast_df['Sales'].values)

def test_task_func_with_different_frequency():
    start_date = '2023-01-01'
    periods = 12
    freq = 'M'
    random_seed = 42
    
    forecast_df, ax = task_func(start_date, periods, freq, random_seed)
    
    # Check if the DataFrame is correctly structured with monthly frequency
    assert isinstance(forecast_df, pd.DataFrame)
    assert 'Sales' in forecast_df.columns
    assert len(forecast_df) == periods
    
    # Check if the DataFrame values are within the expected range
    assert (forecast_df['Sales'] >= 100).all() and (forecast_df['Sales'] <= 500).all()
    
    # Check if the plot is correctly created
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Sales Forecast'
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Sales'
    assert ax.gridOn
    
    # Check if the plot data matches the DataFrame
    plotted_data = ax.lines[0].get_ydata()
    assert np.array_equal(plotted_data, forecast_df['Sales'].values)