import pytest
from src_0918 import task_func
import pandas as pd
from matplotlib.axes import Axes

@pytest.fixture
def sample_data():
    data = {
        'date': pd.date_range(start='2023-01-01', periods=10),
        'closing_price': [100, 102, 101, 105, 107, 110, 112, 115, 117, 120]
    }
    return pd.DataFrame(data)

def test_task_func(sample_data):
    forecast, ax = task_func(sample_data)
    
    # Check that the forecast is a list of 7 floats
    assert isinstance(forecast, list)
    assert len(forecast) == 7
    assert all(isinstance(x, float) for x in forecast)
    
    # Check that ax is an instance of Axes
    assert isinstance(ax, Axes)
    
    # Check that the plot contains the correct labels
    assert ax.get_legend().get_texts()[0].get_text() == 'Historical Closing Prices'
    assert ax.get_legend().get_texts()[1].get_text() == 'Forecasted Closing Prices'
    
    # Check that the plot has the correct number of data points
    historical_data_points = len(sample_data['date'])
    forecast_data_points = len(forecast)
    total_data_points = historical_data_points + forecast_data_points
    assert len(ax.lines[0].get_xdata()) == historical_data_points
    assert len(ax.lines[1].get_xdata()) == forecast_data_points
    assert len(ax.lines[0].get_ydata()) == historical_data_points
    assert len(ax.lines[1].get_ydata()) == forecast_data_points
    
    # Check that the forecast dates are correctly calculated
    expected_forecast_dates = pd.date_range(start=sample_data['date'].iloc[-1] + pd.Timedelta(days=1), periods=7)
    assert all(ax.lines[1].get_xdata() == expected_forecast_dates)