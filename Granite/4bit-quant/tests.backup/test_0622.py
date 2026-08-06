import pytest
from src_0622 import task_func

def test_task_func():
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ax = task_func(L)
    assert ax is not None
    assert ax.get_lines()

def test_task_func_with_empty_list():
    L = [[]]
    ax = task_func(L)
    assert ax is not None
    assert ax.get_lines()

def test_task_func_with_float_values():
    L = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
    ax = task_func(L)
    assert ax is not None
    assert ax.get_lines()

def test_task_func_with_invalid_input():
    L = "invalid input"
    with pytest.raises(TypeError):
        task_func(L)