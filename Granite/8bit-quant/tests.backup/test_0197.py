import pytest
from src_0197 import task_func

def test_task_func_valid_input():
    assert task_func(length=10) is not None

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(length=10, range_limit=1)

def test_task_func_seed():
    plot1, numbers1 = task_func(length=10, seed=0)
    plot2, numbers2 = task_func(length=10, seed=0)
    assert numbers1 == numbers2

def test_task_func_different_seed():
    plot1, numbers1 = task_func(length=10, seed=0)
    plot2, numbers2 = task_func(length=10, seed=1)
    assert numbers1 != numbers2