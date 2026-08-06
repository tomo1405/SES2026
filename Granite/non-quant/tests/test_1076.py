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
    ax = task_func(time_strings)
    bar_heights = ax.patches[0].get_height()
    assert len(bar_heights) == len(expected_differences)
    for actual, expected in zip(bar_heights, expected_differences):
        assert actual == expected

if __name__ == "__main__":
    pytest.main()