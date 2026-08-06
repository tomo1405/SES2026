import matplotlib.pyplot as plt
from src_0063 import task_func


def test_task_func():
    result = [
        {'from_user': 1},
        {'from_user': 2},
        {'from_user': 3},
        {'from_user': 4},
        {'from_user': 5},
    ]
    task_func(result)
    assert plt.figure.called
    assert sns.histplot.called