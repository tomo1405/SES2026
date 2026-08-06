import pytest
from src_0129 import task_func
import numpy as np
import matplotlib.pyplot as plt
from random import randint
import math

def test_task_func():
    POINTS = 100
    x = np.zeros(POINTS)
    y = np.zeros(POINTS)

    for i in range(1, POINTS):
        val = randint(0, 1)
        if val == 1:
            x[i] = x[i - 1] + math.cos(2 * math.pi * val)
            y[i] = y[i - 1] + math.sin(2 * math.pi * val)
        else:
            x[i] = x[i - 1] - math.cos(2 * math.pi * val)
            y[i] = y[i - 1] - math.sin(2 * math.pi * val)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()
    assert fig is not None
    assert ax is not None
    assert len(x) == POINTS
    assert len(y) == POINTS
    assert np.all(x >= 0)
    assert np.all(y >= 0)
    assert np.all(x <= 1)
    assert np.all(y <= 1)