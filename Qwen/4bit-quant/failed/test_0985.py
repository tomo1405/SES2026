import pytest
from src_0985 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    data = {
        'x': [1, 2, 3, 4, 5],
        'y': [2, 4, 6, 8, 10]
    }
    return pd.DataFrame(data)

def test_task_func(sample_data):
    ax = task_func(sample_data, 'x', 'y')
    
    # Check if the plot has been created
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object."
    
    # Check if the scatter plot and regression line are plotted
    lines = ax.get_lines()
    assert len(lines) == 1, "There should be one line (regression line) in the plot."
    scatter = ax.collections[0]
    assert len(scatter.get_offsets()) == len(sample_data), "The number of points in the scatter plot should match the number of rows in the dataframe."
    
    # Check if the regression line is correct
    x_values = sample_data['x'].values.reshape(-1, 1)
    y_values = sample_data['y'].values
    reg = LinearRegression().fit(x_values, y_values)
    y_pred = reg.predict(x_values)
    assert np.allclose(y_pred, lines[0].get_ydata()), "The predicted values from the regression line should match the actual values."

# Run the tests
if __name__ == "__main__":
    pytest.main()