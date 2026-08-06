python
import pytest
from src_0419 import task_func

def test_task_func():
    X = [[1, 2], [3, 4], [5, 6], [7, 8]]
    Y = [0, 1, 0, 1]

    model, ax = task_func(X, Y)

    assert isinstance(model, keras.Sequential)
    assert isinstance(ax, plt.Axes)