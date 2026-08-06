import pytest
from src_0368 import task_func
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt
import io
import sys

def test_task_func_type_error():
    with pytest.raises(TypeError, match='All activities must be datetime objects'):
        task_func(['not a datetime'])

def test_task_func_empty_list():
    ax = task_func([])
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Weekly Activity'
    assert ax.get_xlabel() == 'Day of the Week'
    assert ax.get_ylabel() == 'Number of Activities'
    assert list(ax.get_xticklabels()) == ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    assert list(ax.get_yticklabels()) == ['0']

def test_task_func_single_activity():
    activity = datetime(2023, 10, 9)  # Monday
    ax = task_func([activity])
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Weekly Activity'
    assert ax.get_xlabel() == 'Day of the Week'
    assert ax.get_ylabel() == 'Number of Activities'
    assert list(ax.get_xticklabels()) == ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    assert list(ax.get_yticklabels()) == ['0', '1']

def test_task_func_multiple_activities():
    activities = [
        datetime(2023, 10, 9),  # Monday
        datetime(2023, 10, 10), # Tuesday
        datetime(2023, 10, 11), # Wednesday
        datetime(2023, 10, 12), # Thursday
        datetime(2023, 10, 13), # Friday
        datetime(2023, 10, 14), # Saturday
        datetime(2023, 10, 15)  # Sunday
    ]
    ax = task_func(activities)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Weekly Activity'
    assert ax.get_xlabel() == 'Day of the Week'
    assert ax.get_ylabel() == 'Number of Activities'
    assert list(ax.get_xticklabels()) == ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    assert list(ax.get_yticklabels()) == ['0', '1']

def test_task_func_same_day_activities():
    activities = [
        datetime(2023, 10, 9),  # Monday
        datetime(2023, 10, 9),  # Monday
        datetime(2023, 10, 9),  # Monday
    ]
    ax = task_func(activities)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Weekly Activity'
    assert ax.get_xlabel() == 'Day of the Week'
    assert ax.get_ylabel() == 'Number of Activities'
    assert list(ax.get_xticklabels()) == ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    assert list(ax.get_yticklabels()) == ['0', '1', '2', '3', '4', '5', '6']

def test_task_func_plot_output():
    activities = [
        datetime(2023, 10, 9),  # Monday
        datetime(2023, 10, 10), # Tuesday
        datetime(2023, 10, 11), # Wednesday
    ]
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    ax = task_func(activities)
    sys.stdout = old_stdout
    assert isinstance(ax, plt.Axes)
    assert new_stdout.getvalue() == ''  # No print statements should be outputted