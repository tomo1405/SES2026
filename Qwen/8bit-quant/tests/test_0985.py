import pytest
from src_0985 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def test_task_func():
    # Create a sample DataFrame
    data = {
        'x': [1, 2, 3, 4, 5],
        'y': [2, 4, 6, 8, 10]
    }
    df = pd.DataFrame(data)

    # Call the function
    ax = task_func(df, 'x', 'y')

    # Check if the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, plt.Axes)

    # Check if the plot contains the expected data points and regression line
    lines = ax.get_lines()
    assert len(lines) == 2, "There should be two lines in the plot: one for scatter and one for regression."

    # Extract the scatter and regression line data
    scatter_x, scatter_y = lines[0].get_data()
    regression_x, regression_y = lines[1].get_data()

    # Verify scatter plot data
    assert np.array_equal(scatter_x, df['x'].values), "Scatter plot x-values do not match."
    assert np.array_equal(scatter_y, df['y'].values), "Scatter plot y-values do not match."

    # Verify regression line data
    X = df['x'].values.reshape(-1, 1)
    Y = df['y'].values
    reg = LinearRegression().fit(X, Y)
    Y_pred = reg.predict(X)
    assert np.array_equal(regression_x, X.flatten()), "Regression line x-values do not match."
    assert np.allclose(regression_y, Y_pred), "Regression line y-values do not match."

# Run the test
if __name__ == "__main__":
    pytest.main()