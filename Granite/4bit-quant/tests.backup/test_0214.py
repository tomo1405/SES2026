import pytest
import time
import random
import matplotlib.pyplot as plt
from scipy.stats import kurtosis

def task_func(intervals=100, seed=0):
    random.seed(seed)
    times = []
    numbers = []

    try:
        for _ in range(intervals):
            time.sleep(1)
            times.append(time.time())
            numbers.append(random.random())
    except KeyboardInterrupt:
        print('Interrupted by user')

    kurtosis_value = kurtosis(numbers, nan_policy='omit')
    # Initialize a fresh figure
    plt.figure()
    fig, ax = plt.subplots()
    ax.plot(times, numbers)
    return ax, kurtosis_value

def test_task_func():
    ax, kurtosis_value = task_func()
    assert isinstance(ax, plt.Axes)
    assert isinstance(kurtosis_value, float)
    assert kurtosis_value >= 0
    assert kurtosis_value <= 4

def test_task_func_with_seed():
    ax, kurtosis_value = task_func(seed=42)
    assert isinstance(ax, plt.Axes)
    assert isinstance(kurtosis_value, float)
    assert kurtosis_value >= 0
    assert kurtosis_value <= 4

def test_task_func_with_intervals():
    ax, kurtosis_value = task_func(intervals=50)
    assert isinstance(ax, plt.Axes)
    assert isinstance(kurtosis_value, float)
    assert kurtosis_value >= 0
    assert kurtosis_value <= 4

def test_task_func_with_seed_and_intervals():
    ax, kurtosis_value = task_func(intervals=50, seed=42)
    assert isinstance(ax, plt.Axes)
    assert isinstance(kurtosis_value, float)
    assert kurtosis_value >= 0
    assert kurtosis_value <= 4

def test_task_func_with_seed_and_intervals_and_interrupt():
    with pytest.raises(KeyboardInterrupt):
        task_func(intervals=50, seed=42)