import pytest
from src_0915 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    data = {
        'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'closing_price': [100, 102, 101]
    }
    return pd.DataFrame(data)

def test_task_func(sample_data):
    pred_prices, ax = task_func(sample_data)
    
    # Check if pred_prices is a list of 7 elements
    assert isinstance(pred_prices, list)
    assert len(pred_prices) == 7
    
    # Check if pred_prices are numeric
    assert all(isinstance(price, (int, float)) for price in pred_prices)
    
    # Check if ax is a matplotlib Axes object
    assert isinstance(ax, plt.Axes)
    
    # Check if the plot contains the correct number of lines
    lines = ax.get_lines()
    assert len(lines) == 2  # 1 for scatter and 1 for plot
    
    # Check if the scatter plot has the correct number of points
    scatter_points = ax.collections[0].get_offsets()
    assert len(scatter_points) == 3
    
    # Check if the plot line has the correct number of points
    plot_line = lines[1].get_xdata()
    assert len(plot_line) == 7

# Run the tests
if __name__ == "__main__":
    pytest.main()