import pytest
from src_0197 import task_func

def test_task_func_length():
    length = 10
    range_limit = 100
    seed = 0
    plot, random_numbers = task_func(length, range_limit, seed)
    assert len(random_numbers) == length

def test_task_func_range_limit():
    length = 10
    range_limit = 100
    seed = 0
    plot, random_numbers = task_func(length, range_limit, seed)
    assert all(1 <= x <= range_limit for x in random_numbers)

def test_task_func_seed():
    length = 10
    range_limit = 100
    seed = 0
    plot, random_numbers = task_func(length, range_limit, seed)
    assert random_numbers == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_task_func_plot():
    length = 10
    range_limit = 100
    seed = 0
    plot, random_numbers = task_func(length, range_limit, seed)
    assert isinstance(plot, matplotlib.axes.Axes)
    assert isinstance(random_numbers, list)