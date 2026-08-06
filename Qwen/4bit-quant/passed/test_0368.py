import pytest
from src_0368 import task_func
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt
import io
import sys

@pytest.fixture
def sample_activities():
    return [
        datetime(2023, 10, 2),  # Monday
        datetime(2023, 10, 3),  # Tuesday
        datetime(2023, 10, 4),  # Wednesday
        datetime(2023, 10, 5),  # Thursday
        datetime(2023, 10, 6),  # Friday
        datetime(2023, 10, 7),  # Saturday
        datetime(2023, 10, 8),  # Sunday
    ]

def test_task_func_type_error():
    with pytest.raises(TypeError, match='All activities must be datetime objects'):
        task_func(['not a datetime', datetime.now()])

def test_task_func_correct_counts(sample_activities):
    ax = task_func(sample_activities)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    expected_counts = [1, 1, 1, 1, 1, 1, 1]
    actual_counts = [ax.patches[i].get_height() for i in range(len(days))]
    assert actual_counts == expected_counts

def test_task_func_plot_labels(sample_activities):
    ax = task_func(sample_activities)
    assert ax.get_xlabel() == 'Day of the Week'
    assert ax.get_ylabel() == 'Number of Activities'
    assert ax.get_title() == 'Weekly Activity'

def test_task_func_plot_content(sample_activities):
    ax = task_func(sample_activities)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for i, day in enumerate(days):
        assert ax.patches[i].get_x() == i
        assert ax.patches[i].get_width() == 1
        assert ax.patches[i].get_height() == 1

def test_task_func_plot_output(sample_activities):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    try:
        task_func(sample_activities)
        plt.show()
    finally:
        sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == '', "No output should be printed to stdout"