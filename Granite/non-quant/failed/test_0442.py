import pytest
from src_0442 import task_func
import numpy as np

def test_task_func():
    P = np.array([[1, 2, 3], [4, 5, 6]])
    T = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    expected_result = np.array([[32, 38], [80, 96]])
    expected_ax = "instance of <class 'matplotlib.axes._axes.Axes3D'>"

    result, ax = task_func(P, T)

    assert np.array_equal(result, expected_result)
    assert type(ax) == str(expected_ax)

if __name__ == "__main__":
    pytest.main()