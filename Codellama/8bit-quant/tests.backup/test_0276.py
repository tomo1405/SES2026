import pytest
from src_0276 import task_func

def test_task_func_positive_input():
    n = 5
    expected_output = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
    assert task_func(n) == expected_output

def test_task_func_negative_input():
    n = -1
    with pytest.raises(ValueError):
        task_func(n)