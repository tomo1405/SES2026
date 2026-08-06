import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
from src_0985 import task_func


@pytest.fixture
def sample_df():
    data = {
        'x': np.arange(10),
        'y': np.arange(10) * 2 + np.random.rand(10)
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    ax = task_func(sample_df, 'x', 'y')
    
    # Check if the returned object is a matplotlib Axes
    assert isinstance(ax, plt.Axes)
    
    # Check if the scatter plot and regression line are plotted
    lines = ax.get_lines()
    assert len(lines) == 1, "There should be exactly one line (regression line)"
    scatter_points = ax.collections
    assert len(scatter_points) == 1, "There should be exactly one scatter plot"
    
    # Check if the data points are correctly plotted
    x_data, y_data = scatter_points[0].get_offsets().T
    np.testing.assert_array_equal(x_data, sample_df['x'].values)
    np.testing.assert_array_equal(y_data, sample_df['y'].values)
    
    # Check if the regression line is plotted through the data points
    x_line = lines[0].get_xdata()
    y_line = lines[0].get_ydata()
    np.testing.assert_array_equal(x_line, sample_df['x'].values)
    
    # Additional check to ensure the regression line is correct
    model = LinearRegression().fit(sample_df[['x']], sample_df['y'])
    y_pred = model.predict(sample_df[['x']])
    np.testing.assert_array_almost_equal(y_line, y_pred)