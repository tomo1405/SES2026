import pytest
from src_0918 import task_func
import pandas as pd
import numpy as np
from matplotlib.axes import Axes

@pytest.fixture
def sample_data():
    dates = pd.date_range(start='2023-01-01', periods=10, freq='D')
    closing_prices = np.random.rand(10) * 100
    return pd.DataFrame({'date': dates, 'closing_price': closing_prices})

def test_task_func(sample_data):
    forecast, ax = task_func(sample_data)
    
    # Check if forecast is a list of floats with length 7
    assert isinstance(forecast, list)
    assert all(isinstance(x, float) for x in forecast)
    assert len(forecast) == 7
    
    # Check if ax is an instance of Axes
    assert isinstance(ax, Axes)
    
    # Check if the plot contains the correct number of lines
    lines = ax.get_lines()
    assert len(lines) == 2, "The plot should have two lines: one for historical and one for forecasted prices."

    # Check if the forecasted dates are correctly calculated
    forecast_dates = pd.date_range(start=sample_data['date'].iloc[-1] + pd.Timedelta(days=1), periods=7)
    assert all(forecast_dates[i] == lines[1].get_xdata()[i] for i in range(7)), "Forecasted dates do not match."

    # Check if the forecasted values are plotted correctly
    assert all(forecast[i] == lines[1].get_ydata()[i] for i in range(7)), "Forecasted values do not match."