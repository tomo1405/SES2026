import pytest
from src_0367 import task_func

def test_task_func():
    number_list = [1, 2, 3, 4, 5]
    bins = 5
    ax = task_func(number_list, bins)
    assert ax.get_title() == 'Histogram'
    assert ax.get_xlabel() == 'Number'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_xlim() == (1, 5)
    assert ax.get_ylim() == (0, 5)
    assert ax.get_xticks() == [1, 2, 3, 4, 5]
    assert ax.get_yticks() == [0, 1, 2, 3, 4, 5]
    assert ax.get_xticklabels() == ['1', '2', '3', '4', '5']
    assert ax.get_yticklabels() == ['0', '1', '2', '3', '4', '5']
    assert ax.get_color() == random.choice(COLORS)