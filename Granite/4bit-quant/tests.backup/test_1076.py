import datetime
import numpy as np
import matplotlib.pyplot as plt
from src_1076 import task_func

TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"

def test_task_func():
    time_strings = ["01/01/22 12:00:00.000000", "01/01/22 12:00:01.000000", "01/01/22 12:00:02.000000"]
    expected_differences = np.array([1, 1])

    result = task_func(time_strings)
    assert result is not None
    assert isinstance(result, plt.Axes)
    assert np.array_equal(result.get_xlabel(), "Index")
    assert np.array_equal(result.get_ylabel(), "Time Difference (seconds)")
    assert np.array_equal(result.get_title(), "Time Differences Between Consecutive Timestamps")
    assert np.array_equal(result.patches[0].get_height(), expected_differences)

test_task_func()