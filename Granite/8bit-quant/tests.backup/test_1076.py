import datetime
import numpy as np
import matplotlib.pyplot as plt
from src_1076 import task_func
import pytest

TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"

def test_task_func():
    time_strings = [
        "01/01/22 00:00:00.000000",
        "01/01/22 00:00:01.000000",
        "01/01/22 00:00:02.000000",
        "01/01/22 00:00:03.000000",
        "01/01/22 00:00:04.000000",
    ]
    expected_differences = [1, 1, 1, 1]
    expected_xlabel = "Index"
    expected_ylabel = "Time Difference (seconds)"
    expected_title = "Time Differences Between Consecutive Timestamps"

    result = task_func(time_strings)

    assert isinstance(result, plt.Axes)
    assert np.array_equal(result.patches[0].get_height(), expected_differences)
    assert result.get_xlabel() == expected_xlabel
    assert result.get_ylabel() == expected_ylabel
    assert result.get_title() == expected_title