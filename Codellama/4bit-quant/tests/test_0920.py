import pytest
from src_0920 import task_func

def test_task_func():
    data = {'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10], 'C': [3, 6, 9, 12, 15]}
    column = 'A'
    ax = task_func(data, column)
    assert ax.get_xlabel() == 'Category'
    assert ax.get_ylabel() == 'Count'
    assert ax.get_title() == f'Distribution of {column}'
    assert len(ax.get_xticks()) == 5
    assert len(ax.get_yticks()) == 5
    assert ax.get_xticks()[0] == 'A'
    assert ax.get_xticks()[1] == 'B'
    assert ax.get_xticks()[2] == 'C'
    assert ax.get_xticks()[3] == 'D'
    assert ax.get_xticks()[4] == 'E'
    assert ax.get_yticks()[0] == 0
    assert ax.get_yticks()[1] == 1
    assert ax.get_yticks()[2] == 2
    assert ax.get_yticks()[3] == 3
    assert ax.get_yticks()[4] == 4