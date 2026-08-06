import pytest
from src_0368 import task_func
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

def test_task_func_with_empty_list():
    with pytest.raises(TypeError) as excinfo:
        task_func([])
    assert str(excinfo.value) == 'All activities must be datetime objects'

def test_task_func_with_non_datetime_objects():
    with pytest.raises(TypeError) as excinfo:
        task_func([1, 2, 3])
    assert str(excinfo.value) == 'All activities must be datetime objects'

def test_task_func_with_valid_dates():
    dates = [
        datetime(2023, 10, 2),  # Monday
        datetime(2023, 10, 3),  # Tuesday
        datetime(2023, 10, 4),  # Wednesday
        datetime(2023, 10, 5),  # Thursday
        datetime(2023, 10, 6),  # Friday
        datetime(2023, 10, 7),  # Saturday
        datetime(2023, 10, 8),  # Sunday
        datetime(2023, 10, 9),  # Monday
    ]
    ax = task_func(dates)
    assert isinstance(ax, plt.Axes)
    expected_counts = [2, 1, 1, 1, 1, 1, 1]
    for i, day in enumerate(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']):
        bar_height = ax.patches[i].get_height()
        assert bar_height == expected_counts[i]

def test_task_func_with_all_same_day():
    dates = [
        datetime(2023, 10, 2),  # Monday
        datetime(2023, 10, 9),  # Monday
        datetime(2023, 10, 16), # Monday
    ]
    ax = task_func(dates)
    assert isinstance(ax, plt.Axes)
    expected_counts = [3, 0, 0, 0, 0, 0, 0]
    for i, day in enumerate(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']):
        bar_height = ax.patches[i].get_height()
        assert bar_height == expected_counts[i]

def test_task_func_with_random_dates():
    dates = [
        datetime(2023, 10, 3),  # Tuesday
        datetime(2023, 10, 5),  # Thursday
        datetime(2023, 10, 7),  # Saturday
        datetime(2023, 10, 10), # Tuesday
        datetime(2023, 10, 12), # Thursday
        datetime(2023, 10, 14), # Saturday
    ]
    ax = task_func(dates)
    assert isinstance(ax, plt.Axes)
    expected_counts = [0, 2, 0, 2, 0, 2, 0]
    for i, day in enumerate(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']):
        bar_height = ax.patches[i].get_height()
        assert bar_height == expected_counts[i]