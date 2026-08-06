import pytest
from src_0553 import task_func

def test_task_func():
    a = [1, 2, 3]
    b = [3, 4, 5]
    expected_counts = {'apple': 0, 'banana': 0}
    ax = task_func(a, b)
    for item in ax.patches:
        if item.get_height() != 0:
            expected_counts[item.get_x()] = item.get_height()
    assert ax.patches[0].get_x() == 'apple'
    assert ax.patches[1].get_x() == 'banana'
    assert ax.patches[0].get_height() == expected_counts['apple']
    assert ax.patches[1].get_height() == expected_counts['banana']