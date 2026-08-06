import pytest
from src_0101 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    # Capture the plot object returned by the function
    ax = task_func()

    # Check if the plot object is of the correct type
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object."

    # Check if the x-axis label is set correctly
    assert ax.get_xlabel() == 'Date', "The x-axis label should be 'Date'."

    # Check if the y-axis label is set correctly
    assert ax.get_ylabel() == 'Value', "The y-axis label should be 'Value'."

    # Check if the title is set correctly
    assert ax.get_title() == 'Random Time Series Data', "The title should be 'Random Time Series Data'."

    # Check if the legend is set correctly
    handles, labels = ax.get_legend_handles_labels()
    assert labels == ['Value over Time'], "The legend should have the label 'Value over Time'."

    # Check if there are exactly 30 data points plotted
    lines = ax.get_lines()
    assert len(lines) == 1, "There should be exactly one line plot."
    assert len(lines[0].get_xdata()) == 30, "There should be exactly 30 data points on the x-axis."
    assert len(lines[0].get_ydata()) == 30, "There should be exactly 30 data points on the y-axis."

    # Check if the data points are within the expected range
    y_data = lines[0].get_ydata()
    assert all(0 <= value <= 100 for value in y_data), "All y-values should be between 0 and 100."

    # Check if the x-axis data is a pandas DatetimeIndex
    x_data = lines[0].get_xdata()
    assert isinstance(x_data, pd.DatetimeIndex), "The x-axis data should be a pandas DatetimeIndex."
    assert len(x_data) == 30, "There should be exactly 30 date points on the x-axis."

# Run the tests
if __name__ == "__main__":
    pytest.main()