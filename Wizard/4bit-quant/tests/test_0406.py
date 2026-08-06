python
import random
import matplotlib.pyplot as plt
import pytest

def task_func(points: int):
    x = list(range(points))
    y = [random.random() for _ in range(points)]

    _, ax = plt.subplots()
    ax.plot(x, y)

    return y, ax

def test_task_func():
    y, ax = task_func(10)
    assert len(y) == 10
    assert isinstance(ax, plt.Axes)