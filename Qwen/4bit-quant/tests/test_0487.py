import matplotlib
import pytest
from src_0487 import task_func


def test_task_func_valid_input():
    start_time = 1633072800000  # Example timestamp in milliseconds
    end_time = 1633076400000    # Example timestamp in milliseconds
    step = 900000               # Step in milliseconds (15 minutes)
    trend = 0.1                 # Trend value

    ax = task_func(start_time, end_time, step, trend)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert len(ax.get_lines()) == 1  # Only one line should be plotted

def test_task_func_start_after_end():
    with pytest.raises(ValueError, match="Start time must be before end time"):
        task_func(1633076400000, 1633072800000, 900000, 0.1)

def test_task_func_invalid_step():
    with pytest.raises(ValueError, match="Invalid step value."):
        task_func(1633072800000, 1633076400000, -900000, 0.1)

def test_task_func_no_data_points():
    start_time = 1633072800000  # Example timestamp in milliseconds
    end_time = 1633072800001    # Example timestamp in milliseconds
    step = 900000               # Step in milliseconds (15 minutes)
    trend = 0.1                 # Trend value

    ax = task_func(start_time, end_time, step, trend)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert len(ax.get_lines()) == 0  # No data points should be plotted

def test_task_func_with_zero_trend():
    start_time = 1633072800000  # Example timestamp in milliseconds
    end_time = 1633076400000    # Example timestamp in milliseconds
    step = 900000               # Step in milliseconds (15 minutes)
    trend = 0.0                 # Trend value

    ax = task_func(start_time, end_time, step, trend)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert len(ax.get_lines()) == 1  # Only one line should be plotted

def test_task_func_with_negative_trend():
    start_time = 1633072800000  # Example timestamp in milliseconds
    end_time = 1633076400000    # Example timestamp in milliseconds
    step = 900000               # Step in milliseconds (15 minutes)
    trend = -0.1                # Trend value

    ax = task_func(start_time, end_time, step, trend)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert len(ax.get_lines()) == 1  # Only one line should be plotted