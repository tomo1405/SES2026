import pytest
from src_0918 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from statsmodels.tsa.arima.model import ARIMA
from typing import List, Tuple

def test_task_func():
    # Create a sample dataframe
    df = pd.DataFrame({'date': pd.date_range(start='2022-01-01', end='2022-01-10'),
                       'closing_price': [10, 12, 15, 18, 20, 22, 25, 28, 30, 32]})
    
    # Test that the function returns a tuple with two elements
    forecast, ax = task_func(df)
    assert isinstance(forecast, list)
    assert isinstance(ax, Axes)
    
    # Test that the forecast has the correct length
    assert len(forecast) == 7
    
    # Test that the forecast dates are correct
    assert forecast_dates == pd.date_range(start=df['date'].iloc[-1] + pd.Timedelta(days=1), periods=7)
    
    # Test that the forecast values are within the range of the historical closing prices
    assert all(forecast >= df['closing_price'].min())
    assert all(forecast <= df['closing_price'].max())
    
    # Test that the plot is created correctly
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, Axes)
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Closing Price'
    assert ax.get_title() == 'Forecasted Closing Prices'
    assert len(ax.get_lines()) == 2
    assert ax.get_lines()[0].get_label() == 'Historical Closing Prices'
    assert ax.get_lines()[1].get_label() == 'Forecasted Closing Prices'