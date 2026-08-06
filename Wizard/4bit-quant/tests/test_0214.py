python
import time
import random
import matplotlib.pyplot as plt
from scipy.stats import kurtosis
import pytest

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
    intervals = 100
    seed = 0
    ax, kurtosis_value = task_func(intervals, seed)
    assert len(ax.lines) == 1
    assert len(ax.lines[0].get_data()[0]) == intervals
    assert kurtosis_value > 0