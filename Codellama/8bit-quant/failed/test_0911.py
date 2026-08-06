import pytest
from src_0911 import task_func

def test_task_func_valid_input():
    letters = ['a', 'b', 'c']
    repetitions = [1, 2, 3]
    colors = ['red', 'green', 'blue']
    ax = task_func(letters, repetitions, colors)
    assert ax.get_xlabel() == 'Letters'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_title() == 'Frequency of Letters'
    assert len(ax.get_xticks()) == 3
    assert len(ax.get_yticks()) == 3
    assert ax.get_xticks()[0] == 'a'
    assert ax.get_xticks()[1] == 'b'
    assert ax.get_xticks()[2] == 'c'
    assert ax.get_yticks()[0] == 1
    assert ax.get_yticks()[1] == 2
    assert ax.get_yticks()[2] == 3

def test_task_func_invalid_input():
    letters = ['a', 'b', 'c']
    repetitions = [1, 2, 3]
    colors = ['red', 'green', 'blue']
    with pytest.raises(ValueError):
        task_func(letters, repetitions, colors)