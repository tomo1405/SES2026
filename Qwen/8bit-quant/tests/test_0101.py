import pytest
from src_0101 import task_func
import matplotlib.pyplot as plt
import pandas as pd

def test_task_func():
    # Capture the plot object returned by the function
    ax = task_func()

    # Check if the plot object is an instance of matplotlib.axes._subplots.AxesSubplot
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object"

    # Check if the x-axis label is set correctly
    assert ax.get_xlabel() == 'Date', "X-axis label should be 'Date'"

    # Check if the y-axis label is set correctly
    assert ax.get_ylabel() == 'Value', "Y-axis label should be 'Value'"

    # Check if the title is set correctly
    assert ax.get_title() == 'Random Time Series Data', "Title should be 'Random Time Series Data'"

    # Check if the legend is set correctly
    legend_text = [text.get_text() for text in ax.get_legend().get_texts()]
    assert legend_text == ['Value over Time'], "Legend should contain 'Value over Time'"

    # Check if the plot has data
    lines = ax.get_lines()
    assert len(lines) == 1, "There should be one line in the plot"
    xdata, ydata = lines[0].get_data()
    assert len(xdata) == 30, "There should be 30 data points on the x-axis"
    assert len(ydata) == 30, "There should be 30 data points on the y-axis"
    assert all(isinstance(date, pd.Timestamp) for date in xdata), "All x-axis data should be Timestamp objects"
    assert all(0 <= value <= 100 for value in ydata), "All y-axis data should be between 0 and 100"

# Run the tests
if __name__ == "__main__":
    pytest.main()