python
import pytest
from src_0477 import task_func

def test_task_func():
    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 6, 8, 10]

    popt, ax = task_func(X, Y)

    assert len(popt) == 3
    assert popt[0] > 0
    assert popt[1] > 0
    assert popt[2] > 0
    assert ax is not None