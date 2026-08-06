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
    x_data, y_data = task_func(1)
    assert len(x_data) == len(y_data)
    assert all(isinstance(x, str) for x in x_data)
    assert all(isinstance(y, int) for y in y_data)
    assert all(VALUES_RANGE[0] <= y <= VALUES_RANGE[1] for y in y_data)