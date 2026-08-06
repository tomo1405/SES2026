import pytest
from src_0918 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from statsmodels.tsa.arima.model import ARIMA
from typing import List, Tuple

def test_task_func():
    # Create a sample dataframe
    df = pd.DataFrame({'date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07'],
                       'closing_price': [100, 110, 120, 130, 140, 150, 160]})
    
    # Test the function with the sample dataframe
    forecast, ax = task_func(df)
    
    # Check that the forecast is a list of floats
    assert isinstance(forecast, list)
    assert all(isinstance(x, float) for x in forecast)
    
    # Check that the axes object is an instance of Axes
    assert isinstance(ax, Axes)
    
    # Check that the forecast dates are correct
    assert ax.get_xticks() == pd.date_range(start=df['date'].iloc[-1] + pd.Timedelta(days=1), periods=7)
    
    # Check that the forecast values are correct
    assert ax.get_yticks() == forecast