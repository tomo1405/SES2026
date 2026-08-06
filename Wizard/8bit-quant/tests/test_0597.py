python
import time
from datetime import datetime
from random import randint
import matplotlib.pyplot as plt
import pytest

def task_func(duration):
    # Constants
    VALUES_RANGE = (0, 100)
    PLOT_INTERVAL = 0.1

    plt.ion()
    x_data = []
    y_data = []

    end_time = time.time() + duration
    while time.time() < end_time:
        x_data.append(datetime.now().strftime('%H:%M:%S.%f'))
        y_data.append(randint(*VALUES_RANGE))

        plt.clf()
        plt.plot(x_data, y_data)
        plt.draw()
        plt.pause(PLOT_INTERVAL)

    plt.ioff()
    plt.show()

    return x_data, y_data

def test_task_func():
    # Test with duration of 1 second
    x_data, y_data = task_func(1)
    assert len(x_data) == 10
    assert len(y_data) == 10
    assert all(isinstance(x, str) for x in x_data)
    assert all(isinstance(y, int) for y in y_data)

    # Test with duration of 5 seconds
    x_data, y_data = task_func(5)
    assert len(x_data) == 50
    assert len(y_data) == 50
    assert all(isinstance(x, str) for x in x_data)
    assert all(isinstance(y, int) for y in y_data)

    # Test with duration of 10 seconds
    x_data, y_data = task_func(10)
    assert len(x_data) == 100
    assert len(y_data) == 100
    assert all(isinstance(x, str) for x in x_data)
    assert all(isinstance(y, int) for y in y_data)