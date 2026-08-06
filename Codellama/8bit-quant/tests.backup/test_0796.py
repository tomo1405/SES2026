import pytest
from src_0796 import task_func


def test_task_func_empty_list():
    assert task_func([]) == deque()


def test_task_func_non_empty_list():
    assert task_func([1, 2, 3]) == deque([1, 2, 3])


def test_task_func_numeric_sum():
    assert task_func([1, 2, 3]) == deque([1, 2, 3])
    assert math.sqrt(sum(item for item in task_func([1, 2, 3]) if isinstance(item, (int, float)))) == 3


def test_task_func_non_numeric_sum():
    assert task_func([1, 2, 3, "a"]) == deque([1, 2, 3, "a"])
    assert math.sqrt(sum(item for item in task_func([1, 2, 3, "a"]) if isinstance(item, (int, float)))) == 3