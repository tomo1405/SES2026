import pytest
from src_1074 import task_func
import matplotlib.pyplot as plt
import io
import sys

def test_task_func_valid_times():
    time_strings = ["01/01/2020 12:30:45.123456", "01/01/2020 12:31:45.123456"]
    ax = task_func(time_strings)
    assert isinstance(ax, plt.Axes)

def test_task_func_invalid_times():
    time_strings = ["01/01/2020 12:30:45.123456", "invalid_time_string"]
    ax = task_func(time_strings)
    assert ax is None

def test_task_func_empty_list():
    time_strings = []
    ax = task_func(time_strings)
    assert ax is None

def test_task_func_no_seconds():
    time_strings = ["01/01/2020 12:30:00.000000", "01/01/2020 12:31:00.000000"]
    ax = task_func(time_strings)
    assert isinstance(ax, plt.Axes)

def test_task_func_captures_error():
    time_strings = ["01/01/2020 12:30:45.123456", "invalid_time_string"]
    captured_output = io.StringIO()
    sys.stdout = captured_output
    task_func(time_strings)
    sys.stdout = sys.__stdout__
    assert "Error parsing time strings:" in captured_output.getvalue()