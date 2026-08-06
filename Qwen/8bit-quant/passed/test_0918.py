import pytest
from src_0918 import task_func
import pandas as pd
from matplotlib.axes import Axes

# Mock data for testing
@pytest.fixture
def mock_data():
    data = {
        'date': pd.date_range(start='2023-01-01', periods=10),
        'closing_price': [100, 102, 101, 105, 107, 110, 112, 115, 118, 120]
    }
    return pd.DataFrame(data)

def test_task_func(mock_data):
    forecast, ax = task_func(mock_data)
    
    # Check if forecast is a list of floats
    assert isinstance(forecast, list)
    assert all(isinstance(x, float) for x in forecast)
    
    # Check if ax is an instance of Axes
    assert isinstance(ax, Axes)
    
    # Check if the plot contains the correct labels
    assert 'Historical Closing Prices' in ax.get_legend_handles_labels()[1]
    assert 'Forecasted Closing Prices' in ax.get_legend_handles_labels()[1]
    
    # Check if the forecast has 7 elements
    assert len(forecast) == 7