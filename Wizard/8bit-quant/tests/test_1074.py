python
import time
import matplotlib.pyplot as plt
import pytest

def task_func(time_strings, time_format="%d/%m/%Y %H:%M:%S.%f"):
    try:
        seconds = [time.strptime(ts, time_format).tm_sec for ts in time_strings]
        _, ax = plt.subplots()
        ax.hist(seconds, bins=60, rwidth=0.8)
        return ax
    except ValueError as e:
        print(f"Error parsing time strings: {e}")
        return None

def test_task_func():
    time_strings = ["01/01/2022 12:00:00.000000", "01/01/2022 12:00:00.000001", "01/01/2022 12:00:00.000002"]
    ax = task_func(time_strings)
    assert ax is not None
    assert ax.get_xlabel() == "Seconds"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Histogram of Seconds"
    assert len(ax.patches) == 60
    assert ax.patches[0].get_height() == 1
    assert ax.patches[1].get_height() == 0
    assert ax.patches[2].get_height() == 0
    assert ax.patches[3].get_height() == 0
    assert ax.patches[4].get_height() == 0
    assert ax.patches[59].get_height() == 1