import matplotlib.pyplot as plt
from src_0477 import task_func


def test_task_func():
    X = [1, 2, 3, 4, 5]
    Y = [1, 4, 9, 16, 25]
    expected_popt = [1, 2, 3]
    expected_ax = plt.subplots()

    popt, ax = task_func(X, Y)

    assert popt == expected_popt
    assert ax == expected_ax