python
import pytest
from src_0419 import task_func

def test_task_func():
    X = [[0, 0], [0, 1], [1, 0], [1, 1]]
    Y = [0, 1, 1, 0]

    model, ax = task_func(X, Y)

    assert isinstance(model, keras.Sequential)
    assert isinstance(ax, matplotlib.axes._subplots.AxesSubplot)