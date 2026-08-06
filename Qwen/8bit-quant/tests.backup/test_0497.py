import pytest
from src_0497 import task_func
from datetime import datetime, timedelta
import numpy as np

def test_task_func_default_parameters():
    ax = task_func()
    assert isinstance(ax, plt.Axes)
    dates = [datetime.now().date() - timedelta(days=i) for i in range(7)]
    assert all(isinstance(date, datetime.date) for date in dates)
    temperatures = np.random.randint(low=15, high=35, size=7)
    assert len(temperatures) == 7
    assert all(15 <= temp < 35 for temp in temperatures)

def test_task_func_custom_days_in_past():
    days_in_past = 5
    ax = task_func(days_in_past=days_in_past)
    assert isinstance(ax, plt.Axes)
    dates = [datetime.now().date() - timedelta(days=i) for i in range(days_in_past)]
    assert all(isinstance(date, datetime.date) for date in dates)
    temperatures = np.random.randint(low=15, high=35, size=days_in_past)
    assert len(temperatures) == days_in_past
    assert all(15 <= temp < 35 for temp in temperatures)

def test_task_func_custom_random_seed():
    random_seed = 42
    ax1 = task_func(random_seed=random_seed)
    ax2 = task_func(random_seed=random_seed)
    assert isinstance(ax1, plt.Axes)
    assert isinstance(ax2, plt.Axes)
    dates1 = [datetime.now().date() - timedelta(days=i) for i in range(7)]
    dates2 = [datetime.now().date() - timedelta(days=i) for i in range(7)]
    assert all(date1 == date2 for date1, date2 in zip(dates1, dates2))
    temperatures1 = np.random.randint(low=15, high=35, size=7)
    temperatures2 = np.random.randint(low=15, high=35, size=7)
    assert len(temperatures1) == 7
    assert len(temperatures2) == 7
    assert all(temp1 == temp2 for temp1, temp2 in zip(temperatures1, temperatures2))

def test_task_func_invalid_days_in_past():
    with pytest.raises(ValueError):
        task_func(days_in_past=0)
    with pytest.raises(ValueError):
        task_func(days_in_past=-1)