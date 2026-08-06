import pytest
from src_1076 import task_func
import numpy as np
import matplotlib.pyplot as plt
import datetime

# Mocking matplotlib to capture plot outputs
@pytest.fixture
def mock_plot(monkeypatch):
    class MockBar:
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    class MockGca:
        def get_lines(self):
            return []

    class MockPyplot:
        def bar(self, *args, **kwargs):
            return MockBar(*args, **kwargs)

        def gca(self):
            return MockGca()

    monkeypatch.setattr(plt, 'bar', MockPyplot().bar)
    monkeypatch.setattr(plt, 'gca', MockPyplot().gca)

def test_task_func(mock_plot):
    time_strings = [
        "01/01/23 12:00:00.000000",
        "01/01/23 12:01:00.000000",
        "01/01/23 12:02:00.000000"
    ]
    ax = task_func(time_strings)
    
    # Check if the correct number of bars is plotted
    assert len(ax.get_lines()) == 2  # There should be 2 differences between 3 timestamps

    # Check if the differences are calculated correctly
    expected_differences = [60, 60]  # 1 minute difference between each timestamp
    actual_differences = [line.get_height() for line in ax.get_lines()]
    assert np.array_equal(actual_differences, expected_differences)

    # Check if the plot has the correct labels and title
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Time Difference (seconds)"
    assert ax.get_title() == "Time Differences Between Consecutive Timestamps"