from datetime import datetime

import matplotlib
import pytest
from src_0368 import task_func


def test_task_func_raises_type_error_if_not_all_activities_are_datetime():
    activities = [1, 2, 3]
    with pytest.raises(TypeError):
        task_func(activities)

def test_task_func_returns_ax_if_all_activities_are_datetime():
    activities = [datetime(2022, 1, 1), datetime(2022, 1, 2), datetime(2022, 1, 3)]
    ax = task_func(activities)
    assert isinstance(ax, matplotlib.axes.Axes)

def test_task_func_plots_correct_data():
    activities = [datetime(2022, 1, 1), datetime(2022, 1, 2), datetime(2022, 1, 3)]
    ax = task_func(activities)
    assert ax.get_xlabel() == 'Day of the Week'
    assert ax.get_ylabel() == 'Number of Activities'
    assert ax.get_title() == 'Weekly Activity'
    assert ax.get_xticks() == ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    assert ax.get_yticks() == [1, 2, 3]