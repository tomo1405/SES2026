python
import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt
import pytest

def task_func(data):
    max_y_point = max(data, key=itemgetter(1))
    points = np.array(data)
    x = points[:,0]
    y = points[:,1]

    fig, ax = plt.subplots()
    ax.scatter(x, y, label='Points')
    ax.scatter(*max_y_point, color='red', label='Max Y Point')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Points with Max Y Point Highlighted')
    ax.legend()
    return ax, max_y_point

def test_task_func():
    data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    ax, max_y_point = task_func(data)
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_title() == 'Points with Max Y Point Highlighted'
    assert max_y_point == (7, 8)