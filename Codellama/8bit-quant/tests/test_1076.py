import pytest
from src_1076 import task_func
import datetime
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    time_strings = ["01/01/19 12:00:00.000", "01/01/19 12:00:01.000", "01/01/19 12:00:02.000"]
    expected_differences = [1, 1, 1]
    expected_xlabel = "Index"
    expected_ylabel = "Time Difference (seconds)"
    expected_title = "Time Differences Between Consecutive Timestamps"

    # Test the function
    ax = task_func(time_strings)

    # Check the plot
    assert ax.get_xlabel() == expected_xlabel
    assert ax.get_ylabel() == expected_ylabel
    assert ax.get_title() == expected_title
    assert np.array_equal(ax.get_xticks(), np.arange(len(time_strings)))
    assert np.array_equal(ax.get_yticks(), expected_differences)