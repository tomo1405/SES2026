import pytest
from src_0486 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def mock_plt(mocker):
    mocker.patch('matplotlib.pyplot.subplots', return_value=(plt.figure(), plt.gca()))

def test_task_func(mock_plt):
    start_time = "2023-01-01"
    end_time = "2023-01-05"
    ax = task_func(start_time, end_time)

    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Time difference (hours)"
    assert len(ax.get_lines()) == 5  # Number of timezones

    # Check that each line has the correct label
    labels = [line.get_label() for line in ax.get_lines()]
    assert set(labels) == {"UTC", "America/Los_Angeles", "Europe/Paris", "Asia/Kolkata", "Australia/Sydney"}

    # Check that the dates are correctly plotted
    dates = np.arange(
        datetime.strptime(start_time, "%Y-%m-%d"),
        datetime.strptime(end_time, "%Y-%m-%d"),
        timedelta(days=1)
    ).astype(datetime)
    for date in dates:
        assert any([date == x for x in ax.get_xticks()])

    # Check that the plot is displayed
    plt.show.assert_called_once()

if __name__ == "__main__":
    pytest.main()