import pytest
from src_1076 import task_func
import datetime
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    time_strings = ["01/01/2022 00:00:00.000", "01/01/2022 00:00:01.000", "01/01/2022 00:00:02.000"]
    expected_differences = [1, 1, 1]
    expected_xlabel = "Index"
    expected_ylabel = "Time Difference (seconds)"
    expected_title = "Time Differences Between Consecutive Timestamps"

    # Test the function
    ax = task_func(time_strings)

    # Check the x-axis label
    assert ax.get_xlabel() == expected_xlabel

    # Check the y-axis label
    assert ax.get_ylabel() == expected_ylabel

    # Check the title
    assert ax.get_title() == expected_title

    # Check the bar chart
    assert np.array_equal(ax.get_children()[0].get_height(), expected_differences)