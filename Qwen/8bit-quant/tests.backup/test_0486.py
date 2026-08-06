import pytest
from src_0486 import task_func
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def setup():
    plt.switch_backend('Agg')  # Use Agg backend to avoid GUI issues in headless environments

@pytest.mark.parametrize("start_time, end_time", [
    ("2023-01-01", "2023-01-05"),
    ("2023-06-01", "2023-06-10"),
    ("2023-12-25", "2023-12-31")
])
def test_task_func(setup, start_time, end_time):
    ax = task_func(start_time, end_time)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 5  # There should be 5 lines, one for each timezone

    # Check that the x-axis labels are dates within the given range
    x_labels = [label.get_text() for label in ax.get_xticklabels()]
    start_date = datetime.strptime(start_time, "%Y-%m-%d")
    end_date = datetime.strptime(end_time, "%Y-%m-%d")
    expected_dates = np.arange(start_date, end_date, timedelta(days=1)).astype(datetime)
    expected_dates_str = [date.strftime("%Y-%m-%d") for date in expected_dates]
    assert set(x_labels).issubset(set(expected_dates_str))

    # Check that the y-axis limits are reasonable
    y_min, y_max = ax.get_ylim()
    assert y_min >= -12  # UTC is the reference, so the min difference should be at least -12 hours
    assert y_max <= 14  # The max difference should be less than or equal to 14 hours (Sydney)

    # Check that the legend has the correct labels
    legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
    expected_labels = [
        "UTC",
        "America/Los_Angeles",
        "Europe/Paris",
        "Asia/Kolkata",
        "Australia/Sydney"
    ]
    assert legend_labels == expected_labels

    # Check that the plot has a title and labels
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Time difference (hours)"
    assert ax.get_title() == ""  # No title is set in the original function