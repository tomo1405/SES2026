import pytest
from src_0477 import task_func

def test_task_func():
    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 5, 4, 2]
    expected_popt = [1.9999999999999998, 0.9999999999999998, 1.9999999999999998]
    expected_ax = "instance of <class 'matplotlib.axes._subplots.AxesSubplot'>"

    popt, ax = task_func(X, Y)

    assert popt == expected_popt
    assert type(ax) == str(expected_ax)

if __name__ == "__main__":
    pytest.main()