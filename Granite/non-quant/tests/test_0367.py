import random

from src_0367 import task_func


def test_task_func():
    number_list = [random.randint(1, 100) for _ in range(100)]
    bins = 10
    ax = task_func(number_list, bins)
    assert ax is not None
    assert ax.get_title() == 'Histogram'
    assert ax.get_xlabel() == 'Number'
    assert ax.get_ylabel() == 'Frequency'