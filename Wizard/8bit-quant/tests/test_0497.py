python
import pytest
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt

def task_func(days_in_past=7, random_seed=0):
    np.random.seed(random_seed)

    if days_in_past < 1:
        raise ValueError("days_in_past must be in the past")

    dates = [datetime.now().date() - timedelta(days=i) for i in range(days_in_past)]
    temperatures = np.random.randint(low=15, high=35, size=days_in_past)

    fig, ax = plt.subplots()
    ax.plot(dates, temperatures)
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Temperature Trend")
    return ax

def test_task_func():
    # Test with default arguments
    ax = task_func()
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 1
    assert ax.lines[0].get_data()[0].size == 7
    assert ax.lines[0].get_data()[1].size == 7
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Temperature (°C)"
    assert ax.get_title() == "Temperature Trend"

    # Test with custom arguments
    ax = task_func(days_in_past=30, random_seed=42)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 1
    assert ax.lines[0].get_data()[0].size == 30
    assert ax.lines[0].get_data()[1].size == 30
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Temperature (°C)"
    assert ax.get_title() == "Temperature Trend"

    # Test with invalid arguments
    with pytest.raises(ValueError):
        task_func(days_in_past=0)