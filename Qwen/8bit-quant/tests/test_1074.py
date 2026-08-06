import pytest
from src_1074 import task_func
import matplotlib.pyplot as plt
import io
import sys

def test_task_func_valid_input():
    time_strings = ["01/01/2020 12:34:56.789012", "01/01/2020 12:35:01.234567"]
    ax = task_func(time_strings)
    assert isinstance(ax, plt.Axes)
    plt.close()

def test_task_func_invalid_input():
    time_strings = ["01/01/2020 12:34:56.789012", "invalid_time_string"]
    ax = task_func(time_strings)
    assert ax is None

def test_task_func_no_time_strings():
    time_strings = []
    ax = task_func(time_strings)
    assert ax is None

def test_task_func_different_time_format():
    time_strings = ["2020-01-01 12:34:56.789012", "2020-01-01 12:35:01.234567"]
    ax = task_func(time_strings, time_format="%Y-%m-%d %H:%M:%S.%f")
    assert isinstance(ax, plt.Axes)
    plt.close()

def test_task_func_captures_error_output(capsys):
    time_strings = ["01/01/2020 12:34:56.789012", "invalid_time_string"]
    task_func(time_strings)
    captured = capsys.readouterr()
    assert "Error parsing time strings:" in captured.out

def test_task_func_plot_not_shown(monkeypatch):
    time_strings = ["01/01/2020 12:34:56.789012", "01/01/2020 12:35:01.234567"]
    monkeypatch.setattr(plt, 'show', lambda: None)
    ax = task_func(time_strings)
    assert isinstance(ax, plt.Axes)
    plt.close()