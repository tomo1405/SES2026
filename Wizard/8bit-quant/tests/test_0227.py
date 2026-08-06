python
import numpy as np
import math
import matplotlib.pyplot as plt

def task_func(range_start=0, range_end=10, step=0.1):
    x_values = np.arange(range_start, range_end, step)
    data = ((x, math.exp(x)) for x in x_values)
    _, ax = plt.subplots()
    for x, exp_x in data:
        ax.scatter(x, exp_x, color='b')
    ax.set_title("Exponential Function Plot")
    ax.set_xlabel("x")
    ax.set_ylabel("e^x")
    return data, ax

def test_task_func():
    data, ax = task_func()
    assert len(data) == 101
    assert data[0][0] == 0
    assert data[-1][0] == 10
    assert data[0][1] == 1
    assert data[-1][1] == math.exp(10)
    assert ax.get_title() == "Exponential Function Plot"
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "e^x"